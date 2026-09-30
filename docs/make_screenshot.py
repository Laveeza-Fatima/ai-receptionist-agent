"""Regenerate docs/demo.png from index.html?autoplay using headless Chrome."""
import pathlib, subprocess, tempfile

root = pathlib.Path(__file__).resolve().parent.parent
chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
out = root / "docs" / "demo.png"
subprocess.run([
    chrome, "--headless=new", "--disable-gpu", "--hide-scrollbars",
    f"--user-data-dir={pathlib.Path(tempfile.gettempdir()) / 'nova_shot_profile'}",
    "--window-size=1280,860", "--virtual-time-budget=15000", "--force-prefers-reduced-motion",
    f"--screenshot={out}", (root / "index.html").as_uri() + "?autoplay",
], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
print("saved" if out.exists() else "failed", out)
