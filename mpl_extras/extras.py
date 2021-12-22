
__all__ = [
    "params",
    "setup_mpl",
]


from matplotlib import texmanager
import matplotlib.pyplot as plt
import tempfile
import logging
import atexit
import shutil
import sys
import os


params = dict(direction="in", left=True, right=True, top=True, bottom=True)


def setup_mpl(fontsize=16, tex=False, cache=False):
    plt.rc("font", **dict(family="serif", size=fontsize))
    plt.rc("text", usetex=tex)
    if cache:
        __tex_cache()


def __tex_cache():
    # QUICK FIX FOR MPL's TEX CACHE IN MULTIPROCESSING

    mpldir = tempfile.mkdtemp()
    atexit.register(shutil.rmtree, mpldir)
    umask = os.umask(0)
    os.umask(umask)
    os.chmod(mpldir, 0o777 & ~umask)
    os.environ["HOME"] = mpldir
    os.environ["MPLCONFIGDIG"] = mpldir

    class TexManager(texmanager.TexManager):
        texcache = os.path.join(mpldir, "tex.cache")

    texmanager.TexManager = TexManager

