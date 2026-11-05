<p align="center">
  <img src="assets/header.svg" alt="Arpit Singh Mann — animated exact solution of the Sod shock tube" width="100%">
</p>

<p align="center">
  <a href="https://arpitmann.com"><img src="https://img.shields.io/badge/site-arpitmann.com-0969da?style=flat-square" alt="Website"></a>
  <a href="mailto:connect@arpitmann.com"><img src="https://img.shields.io/badge/email-connect%40arpitmann.com-0969da?style=flat-square" alt="Email"></a>
  <a href="https://orcid.org/0000-0002-6814-2166"><img src="https://img.shields.io/badge/ORCID-0000--0002--6814--2166-a6ce39?style=flat-square&logo=orcid&logoColor=white" alt="ORCID"></a>
  <a href="https://www.linkedin.com/in/arpit-singh-mann-06ab891a2"><img src="https://img.shields.io/badge/LinkedIn-Arpit%20Singh%20Mann-0a66c2?style=flat-square" alt="LinkedIn"></a>
</p>

I'm an M.Sc. Astronomy student at IIT Indore (B.Sc. Physics Hons, Shivaji College, University of Delhi), working toward computational astrophysics. I like building things end to end: the physics or the model, the code that runs it, and something people can actually open and use.

### Right now

- Learning how astrophysical hydro codes work from the inside, starting with the Sod shock tube in [PLUTO](http://plutocode.ph.unito.it/) (the animation above is its exact solution).
- Starting a winter project with KU Leuven on spectral-line reconstruction of AGB-star winds with the `pomme` code.

### Projects

> Click any project to open the details.

<details>
<summary><b>🌍 EEJ storm forecaster</b> · LSTM forecast of storm-time geomagnetic activity over India</summary>
<br>

Predicts the SYM-H storm index 60 minutes ahead from NASA OMNI solar-wind data, for use in Equatorial Electrojet studies over the Indian sector.

- Started from an XGBoost baseline, then moved to an LSTM trained with an intensity-weighted loss, which improved MAE on intense storms by about 32%.
- Split storms by solar cycle rather than at random, so the model is tested on storms it could not have seen.
- Documented where it fails: the extreme May 2024 storm (Solar Cycle 25, SYM-H −518 nT) lies outside the training distribution, and the model does not handle it well.
- Served as a FastAPI service with a web dashboard.

**Stack:** Python · LSTM · XGBoost · FastAPI

<a href="https://zenodo.org/records/20351375"><img src="https://img.shields.io/badge/model%20%26%20code-Zenodo-1682d4?style=flat-square" alt="Zenodo"></a>
<a href="https://arpitmann.com/eej"><img src="https://img.shields.io/badge/dashboard-arpitmann.com%2Feej-0969da?style=flat-square" alt="Dashboard"></a>

</details>

<details>
<summary><b>🤖 <a href="https://github.com/arpitmann/offaxis-robot">offaxis-robot</a></b> · a 3D robot that mirrors your face, hands and body through your webcam</summary>
<br>

Uses head tracking and off-axis projection so the screen behaves like a window: lean, and you see around the robot. It mirrors blinks, smiles, head turns, fingers and full-body poses, and reacts to gestures like thumbs-up and claps.

- Desktop version in Python (pygame, MediaPipe Holistic); web and phone version in three.js with MediaPipe Tasks.
- Works offline as an installable web app.

**Stack:** Python · JavaScript · three.js · MediaPipe

<a href="https://arpitmann.github.io/offaxis-robot/"><img src="https://img.shields.io/badge/▶%20try%20it-live%20demo-2da44e?style=flat-square" alt="Live demo"></a>

</details>

<details>
<summary><b>🔭 <a href="https://github.com/arpitmann/astro-jobwatch">astro-jobwatch</a></b> · a Telegram bot that finds astronomy PhD positions every night</summary>
<br>

Checks about 150 job boards, registers and university pages nightly, ranks openings by level, field and each user's research interests, removes duplicates and expired listings, and sends deadline reminders.

- Runs on GitHub Actions with versioned JSON state; no server needed.
- Invite-only, with per-user preferences. The showcase repo documents the design; the code itself is private.

**Stack:** Python · Telegram Bot API · GitHub Actions · BeautifulSoup

</details>

<details>
<summary><b>🖼️ <a href="https://github.com/arpitmann/heic-mov-converter">heic-mov-converter</a></b> · a Mac app that turns iPhone HEIC photos and MOV videos into JPG and MP4</summary>
<br>

Keeps EXIF metadata, colour profiles and orientation. Normal iPhone videos are remuxed without re-compression, so conversion is fast and lossless; only formats MP4 can't hold are re-encoded. Everything runs offline.

- GitHub Actions builds, self-tests and packages separate Apple Silicon and Intel `.dmg` installers.

**Stack:** Python · Tk · Pillow · FFmpeg · PyInstaller

<a href="https://github.com/arpitmann/heic-mov-converter/releases"><img src="https://img.shields.io/badge/download-.dmg-2da44e?style=flat-square" alt="Download"></a>

</details>

<details>
<summary><b>🔫 <a href="https://github.com/arpitmann/gunboard">gunboard</a></b> · every keypress is a gunshot</summary>
<br>

A system-wide keyboard listener where letters fire a shotgun, numbers a pistol and symbols a sniper rifle. There are no audio files: every sound is synthesised at startup from filtered noise, pitch sweeps and decay envelopes, and overlapping shots are mixed in real time.

**Stack:** Python · NumPy · sounddevice · pynput

</details>

### Latest activity

<!-- updated automatically every day by .github/workflows/activity.yml -->
<!--ACTIVITY:START-->
- `20 Oct 2026` pushed 1 commit to [gunboard](https://github.com/arpitmann/gunboard)
- `18 Oct 2026` pushed 1 commit to [heic-mov-converter](https://github.com/arpitmann/heic-mov-converter)
- `16 Oct 2026` pushed 1 commit to [astro-jobwatch](https://github.com/arpitmann/astro-jobwatch)
- `13 Oct 2026` pushed 1 commit to [offaxis-robot](https://github.com/arpitmann/offaxis-robot)
- `06 Oct 2026` starred [Off-Axis-Projection-demo](https://github.com/neorxprod/Off-Axis-Projection-demo)
<!--ACTIVITY:END-->

<details>
<summary><b>Tools I use</b></summary>
<br>

Python (NumPy, Matplotlib), Jupyter, PLUTO, Git and GitHub Actions, self-hosted Linux servers, Cloudflare.

</details>
