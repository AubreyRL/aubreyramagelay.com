# aubreyramagelay.com

Static site. Four self-contained HTML pages: styles and script are inlined
in each page, so any file opens and renders correctly on its own.

    index.html    landing page and main gallery
    bio.html      bio and artist statement
    cv.html       education, awards, residencies, exhibitions
    links.html    socials, commissions, plus dormant slots
    CNAME         custom domain for GitHub Pages
    images/       the paintings

## Design

Taken from the Modern Mythology catalogue: white ground, Space Grotesk,
and the blue bar (#1973eb) clipping the top of each heading. Each series can
carry its own accent: Ophic Metamorphosis uses the gold from its catalogue
(#b8901c), Universal Meditations a muted sage (#7c8d84), Fractured Visions
a vermillion taken from the postbox (#d4331a). Set with `data-accent`.

Universal Meditations also carries `data-mood="zen"`: a narrower measure,
two columns, far more space between works, centred captions and no prices.
Add that attribute to any section that should read more quietly.
Fractured Visions carries `data-mood="fractured"`, which doubles the heading
bar into an offset echo.

## The paintings

62 works are in place: 26 Modern Mythology, 22 Ophic Metamorphosis,
9 Universal Meditations and 5 Fractured Visions. The two catalogue series
carry dimensions and prices; Universal Meditations and Fractured Visions
have titles only, awaiting dimensions, years and prices.
To remove prices, delete every line matching `<span class="p">...</span>`.

Catalogue images are 664px (Modern Mythology) and 864px (Ophic) on the long
edge, which is fine at gallery size but soft when opened full screen.
Replacing them with originals is a straight swap: same filename, same folder.

Series without images are listed together in a Forthcoming block at the
foot of the gallery: Recent Works, Mythic Landscapes, Bodies and Water.
No empty slots, no dashed boxes. When a series is ready it moves up into
the gallery proper.

## Deploying

1. Create a public repo on GitHub.
2. Upload every file here, keeping `images/` as a folder.
3. Settings > Pages > Source: Deploy from a branch > `main` / `root`.
4. Free preview address: `https://yourusername.github.io/reponame/`
   Do not upload CNAME until you are ready to switch the domain over.

## Porkbun DNS, when ready

Delete the Jimdo CNAME, any URL forwarding, and any ALIAS record pointing
at uixie.porkbun.com first.

    Type    Host    Answer
    A       (blank) 185.199.108.153
    A       (blank) 185.199.109.153
    A       (blank) 185.199.110.153
    A       (blank) 185.199.111.153
    CNAME   www     yourusername.github.io

Then set the custom domain in Settings > Pages and tick Enforce HTTPS.
