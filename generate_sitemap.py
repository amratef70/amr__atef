#!/usr/bin/env python3
# Simple sitemap generator for a small static site.
# Usage: python generate_sitemap.py > sitemap.xml

import datetime

BASE = "https://amratef70.github.io/amr__atef"
pages = [
    "/",
    # add more pages here, e.g. "/about.html"
]

now = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
print('<?xml version="1.0" encoding="UTF-8"?>')
print('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
for p in pages:
    print("  <url>")
    print(f"    <loc>{{BASE}}{{p}}</loc>")
    print(f"    <lastmod>{{now}}</lastmod>")
    print("    <changefreq>monthly</changefreq>")
    print("    <priority>0.5</priority>")
    print("  </url>")
print("</urlset>")
