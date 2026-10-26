# Privacy Policy

**Media Downloader** (the Windows app, and its browser extension for Chrome, Edge and Brave)

Last updated: October 26, 2026

Media Downloader is a Windows desktop app. It runs on your own PC. It has no account, we don't run a server that
receives your data, and it doesn't collect or send any usage or tracking information. We don't sell or share your data
with anyone.

## What the app connects to

- **The sites you download from.** When you analyze or download a link, the app (through yt-dlp, or gallery-dl for
  pictures and posts) connects to that site, as your browser would, to read the video, pictures or post and download
  them. Each site has its own privacy policy.
- **SponsorBlock**, only when you tick **Cut sponsors** or make a PiP video of a YouTube video: the app sends the
  video's ID to `sponsor.ajay.app` to learn which parts viewers marked as sponsors. Nothing else is sent.
- **Its tools' download sites**, to download and update what it needs: GitHub (yt-dlp, aria2, ffmpeg from gyan.dev's
  GitHub mirror, and new versions of Media Downloader itself), www.gyan.dev (ffmpeg, when GitHub can't be read),
  dl.deno.land (Deno, for YouTube) and codeberg.org (gallery-dl, for pictures and posts). They only learn that a copy
  is being downloaded, as for any download from your browser. Turn off update checks in Settings if you don't want the
  app to check for new versions when it starts.
- **A few well-known sites** (www.google.com, github.com, www.microsoft.com, www.cloudflare.com, www.bing.com,
  www.baidu.com and www.apple.com, asked together; the first to answer is used), to learn today's date for the free
  days and the license (from the date on the answer, not your PC's clock). This is a plain request for the home
  page's headers: nothing about you, your license or your PC is sent.

If you set a proxy in Settings, these connections go through it.

## The browser extension

The extension does nothing until you click its button, or **Download with Media Downloader** in the right-click menu.
Then it sends, only to the Media Downloader app on your PC (never over the internet):

- the address of the page, or of the link you right-clicked;
- your browser's cookies for that one site (for example all of youtube.com's), so the app is signed in to it as you
  are in the browser.

It doesn't read or send anything else: not your history, your other tabs, the pages you visit or the cookies of other
sites. To read a site's cookies, the browser needs it to have access to all sites, which is why it warns, when you add
the extension, that it can "read and change all your data on all websites". It uses that access only for the cookies
of the site you click on.

## Cookies

Posts and videos that need a sign-in can be downloaded with your cookies, only if you choose so:

- **From Tools > Sign in to sites:** the site opens in a separate Edge, Chrome or Brave window, with a new, empty
  profile made for it: your own browser's profile, history and cookies aren't read. Once you have signed in, that
  site's cookies are saved in `%LOCALAPPDATA%\MediaDownloader\sign-ins`, and the window's profile is deleted. The same
  window lets you remove a saved sign-in.
- **From the browser extension:** the cookies it sends (above) are kept in
  `%LOCALAPPDATA%\MediaDownloader\browser-cookies` while the app is open, and deleted when you close it. Each time
  you send a link from a site, that site's cookies replace the ones kept for it.
- **From your browser, chosen in Settings:** the app (through yt-dlp) reads the cookies of the browser you pick, on
  your PC, each time it reads or downloads a link.
- **From a file, or pasted, in Settings:** the same, from the cookies.txt file you choose; pasted cookies are kept in
  `%LOCALAPPDATA%\MediaDownloader\cookies.txt`.

All of them are given to yt-dlp and gallery-dl, and sent only to the site they belong to, as your browser would send them. Cookies are never sent to us
or anywhere else. The cookies the app keeps are on this PC only (`%LOCALAPPDATA%`, which Windows doesn't copy to other
PCs with a roaming profile), and uninstalling the app deletes them all.

## Your license

The license key is checked on your PC: no license server is involved. Your key, and the dates the free days and the
license are counted by, are kept on your PC, encrypted by Windows. The License window shows your PC's **machine
code**, made from Windows' own ID for the installation, so it says nothing about you or the PC itself. It is only sent
if you choose to email it to us, to get a key for that PC; we keep it, with your email address, only to send you your
key and support.

## Where it is stored

Everything stays on your PC:

- Your settings, in `%APPDATA%\MediaDownloader\settings.json`.
- The list of what you downloaded (each one's site and ID, e.g. `youtube dQw4w9WgXcQ`), in
  `%APPDATA%\MediaDownloader\downloaded.txt`, so a playlist or channel opened again shows which ones you already have.
- The download queue (each download's link, title, options and where it was saved), in
  `%APPDATA%\MediaDownloader\queue.json`, so it comes back the next time the app starts. Remove downloads from the
  list, or press Clear finished, to take them out of it.
- ffmpeg, Deno, gallery-dl and aria2, in `%LOCALAPPDATA%\MediaDownloader`, with the cookies (above): pasted cookies,
  the sites you signed in to, and the extension's while the app is open.
- Your license key, in `%LOCALAPPDATA%\MediaDownloader\license.dat`, encrypted for your Windows user.
- Your downloads, in the folder you choose.

A download's log stays in the app's memory and is gone when you close it, unless you save it yourself.

## Deleting your data

1. Remove the extension, if you added it: in the browser, open `chrome://extensions` (`edge://extensions`,
   `brave://extensions`) and press **Remove** on Media Downloader.
2. Uninstall Media Downloader in Windows (**Settings > Apps**). This deletes all the cookies it kept: pasted cookies,
   the sites you signed in to, and the extension's.
3. Delete the folders `%APPDATA%\MediaDownloader` (settings, the queue, the list of what you downloaded) and
   `%LOCALAPPDATA%\MediaDownloader` (ffmpeg, Deno, gallery-dl, aria2 and your license key). Uninstalling leaves them,
   so a reinstall keeps your settings and license.

Your downloads stay in their folder until you delete them.

If you want us to delete your emails, the machine code and license details we hold, or you have any question about your
data, write to **khanh1985@gmail.com**. We delete them within 30 days and reply to confirm.

## Contact

- Email: **khanh1985@gmail.com**
- Phone: +84 985 884 764
