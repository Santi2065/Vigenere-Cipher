"""Re-runs the key-recovery analysis on encrypted.txt with the repository's own functions
and regenerates the figures and numbers shown in the README.

    pip install matplotlib
    python docs/figures/make_figures.py
"""
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
for f in Path("/usr/share/fonts/lm").glob("lm*10-*.otf"):  # Latin Modern, if installed
    font_manager.fontManager.addfont(str(f))
plt.style.use(HERE / "paper.mplstyle")
C = plt.rcParams["axes.prop_cycle"].by_key()["color"]

sys.dont_write_bytecode = True  # keep the repository clean
sys.path.insert(0, str(ROOT))
import key_brute_forcing as kb  # noqa: E402
from decryptor import descifrado_vi  # noqa: E402
from encryptor import cifrado_vi  # noqa: E402


def save(fig, name):
    fig.savefig(HERE / name, metadata={"Date": None})
    plt.close(fig)


raw = (ROOT / "encrypted.txt").read_text(encoding="utf-8")
text = kb.text_formatter(raw)
lengths = range(1, 31)
ioc = {n: kb.ioc_promedio_clave(text, n) for n in lengths}
key_len = max(lengths, key=lambda n: (round(ioc[n], 3), -n))  # shortest length at the IoC plateau
columns = [kb.text_divisor(text, i, key_len) for i in range(key_len)]
freqs = [kb.frecuencia(kb.cuento_repeticion(col), len(col)) for col in columns]
key = "".join(kb.forzar_clave(f) for f in freqs)
plain = descifrado_vi(raw, key)
assert cifrado_vi(plain, key) == raw  # re-encrypting the plaintext gives back encrypted.txt

print(f"letters analysed: {len(text)}")
print("mean IoC per key length:", {n: round(v, 4) for n, v in ioc.items()})
print(f"key length: {key_len}, recovered key: '{key}'")
print("plaintext starts:", plain[:40].replace("\n", " | "))

# ---- Figure 1: Friedman test
fig, ax = plt.subplots(figsize=(7.2, 2.6))
ax.bar(list(lengths), [ioc[n] for n in lengths], width=0.7,
       color=[C[1] if n % key_len == 0 else C[0] for n in lengths])
for y, lab in ((0.0686, "English, 0.0686"), (0.0385, "uniform, 1/26 = 0.0385")):
    ax.axhline(y, color="#1a1a1a", lw=0.7, ls="--")
    ax.text(1.01, y, lab, va="center", fontsize=8, transform=ax.get_yaxis_transform())
ax.set_xlabel("candidate key length $n$")
ax.set_ylabel("mean IoC of the $n$ columns")
ax.set_xlim(0.3, 30.7)
ax.set_ylim(0, 0.08)
ax.set_xticks([1, 5, 10, 15, 20, 25, 30])
save(fig, "fig1-ioc.svg")

# ---- Figure 2: frequency analysis per column
letters = kb.ABECEDARIO
fig, axes = plt.subplots(2, 3, figsize=(7.2, 3.9), sharey=True)
axes = axes.ravel()
axes[0].bar(range(26), [kb.ENGLISH_LETTERS_FRECUENCIES[c] for c in letters], color="#4d4d4d", width=0.75)
axes[0].bar(4, kb.ENGLISH_LETTERS_FRECUENCIES["e"], color=C[1], width=0.75)
axes[0].set_title("(a) English reference")
for i, (ax, f, k) in enumerate(zip(axes[1:], freqs, key)):
    peak = max(range(26), key=lambda j: f[letters[j]])
    ax.bar(range(26), [f[c] for c in letters], color=C[0], width=0.75)
    ax.bar(peak, f[letters[peak]], color=C[1], width=0.75)
    ax.annotate(f"'{letters[peak]}' = 'e' + {letters.index(k)}", (peak, f[letters[peak]]),
                xytext=(0, 2), textcoords="offset points", ha="center", fontsize=7.5)
    ax.set_title(f"({'bcdef'[i]}) column {i + 1}: key letter '{k}'")
for ax in axes:
    ax.set_xticks(range(0, 26, 5), [letters[j] for j in range(0, 26, 5)])
    ax.set_xlim(-0.8, 25.8)
    ax.tick_params(top=False)
for ax in axes[::3]:
    ax.set_ylabel("frequency")
axes[0].set_ylim(0, 0.155)
fig.tight_layout()
save(fig, "fig2-frequencies.svg")
