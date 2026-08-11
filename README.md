# aubreyramagelay.com

Static site. Four self-contained HTML pages. Styles and script are inlined
in each page, so any file opens and renders correctly on its own.

    index.html    landing page and main gallery (five series)
    bio.html      bio and artist statement
    cv.html       education, awards, residencies, exhibitions
    links.html    socials, plus dormant slots for books and Patreon
    CNAME         custom domain for GitHub Pages
    images/       all paintings live here

## Adding paintings

Drop files into `images/` using the names already in the HTML:

    recent-01.jpg     ... recent-06.jpg
    mythology-01.jpg  ... mythology-09.jpg
    landscapes-01.jpg ... landscapes-06.jpg
    ophic-01.jpg      ... ophic-09.jpg
    earlier-01.jpg    ... earlier-06.jpg

Any slot with no file shows a dashed placeholder with the filename in it,
so nothing breaks while the gallery fills up. Long edge around 2000px, JPEG,
under about 500kb each keeps the page quick.

To change a caption, edit the `<figcaption>` for that figure:

    <figcaption><span class="t">Title</span><span class="d">Oil on linen · 100 × 80 cm · 2025</span></figcaption>

To add more works to a series, copy any whole `<figure class="work">` block
and change the filename.

## Deploying

1. Create a public repo on GitHub.
2. Upload every file in this folder, keeping `images/` as a folder.
3. Settings → Pages → Source: Deploy from a branch → `main` / `root`.
4. Settings → Pages → Custom domain: `www.aubreyramagelay.com`, then tick
   Enforce HTTPS once the certificate is issued.

## Porkbun DNS

Delete any existing A, ALIAS or CNAME records for the root and www first.

    Type    Host    Answer
    A       (blank) 185.199.108.153
    A       (blank) 185.199.109.153
    A       (blank) 185.199.110.153
    A       (blank) 185.199.111.153
    CNAME   www     <your-github-username>.github.io

Propagation is usually minutes, occasionally a few hours.
