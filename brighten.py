"""
Corrects the white point of photographed paintings.

The problem in these files is not that the paintings are dark, it is that the
camera never reached white. Several images top out around 60 percent
brightness, so every tone in them is squashed into the bottom of the range.

This measures each image's real highlight and lifts it toward a proper white,
with a soft shoulder so nothing clips, and a capped gain so a genuine night
scene stays a night scene. Blacks are left alone.
"""

import sys, glob, os
import numpy as np
from PIL import Image

TARGET   = 246.0   # where the brightest paint should land
MAX_GAIN = 1.55    # ceiling, so dark canvases are not bleached
PCT      = 99.6    # highlight measured here, ignores stray specular dots


def soft_shoulder(x, knee=0.82):
    """Scale linearly to the knee, then ease into 1.0 so highlights never clip."""
    out = x.copy()
    hi = x > knee
    span = 1.0 - knee
    out[hi] = knee + span * np.tanh((x[hi] - knee) / span)
    return np.clip(out, 0.0, 1.0)


def correct(path, outdir):
    im = Image.open(path).convert('RGB')
    a = np.asarray(im, dtype=np.float32)

    lum = 0.2126 * a[..., 0] + 0.7152 * a[..., 1] + 0.0722 * a[..., 2]
    hi = float(np.percentile(lum, PCT))

    gain = 1.0 if hi <= 0 else min(TARGET / hi, MAX_GAIN)
    gain = max(gain, 1.0)  # never darken

    if gain <= 1.01:
        im.save(os.path.join(outdir, os.path.basename(path)),
                quality=90, subsampling=0, optimize=True)
        return os.path.basename(path), 1.0, hi, hi

    out = soft_shoulder(a / 255.0 * gain) * 255.0
    res = Image.fromarray(np.rint(out).astype(np.uint8))
    res.save(os.path.join(outdir, os.path.basename(path)),
             quality=90, subsampling=0, optimize=True)

    b = np.asarray(res, dtype=np.float32)
    nl = 0.2126 * b[..., 0] + 0.7152 * b[..., 1] + 0.0722 * b[..., 2]
    return os.path.basename(path), gain, hi, float(np.percentile(nl, PCT))


if __name__ == '__main__':
    indir, outdir = sys.argv[1], sys.argv[2]
    os.makedirs(outdir, exist_ok=True)
    print('%-20s %6s %8s %8s' % ('file', 'gain', 'was', 'now'))
    for f in sorted(glob.glob(os.path.join(indir, '*.jpg'))):
        n, g, was, now = correct(f, outdir)
        print('%-20s %6.2f %8.0f %8.0f' % (n, g, was, now))
