import matplotlib
import numpy as np
import os
from tqdm import tqdm
import astropy.io.fits as pyfits
import matplotlib as mpl
import matplotlib.pyplot as plt
import subprocess

def plot(plotfile = '/its/home/sp624/waves_masking/mangle_code_v2/waves_polygon_mask/plots/waves_wide_N_full_mask_graphics.dat',
         fill=1, grey_max=1,
         plot_size=(100, 10), plot_file='waves_n_mask_final.png'):
    """
    Plot mangle polygon file.
    fill = 0: boundaries only, 1: completeness grey-scale, 2: black.
    grey_max gives grey level for unit completenes (0=white, 1 = black)
    """

    def ipanel(ra):
        """Return panel number 1, 2 or 3 corresponding to G09, G12, G15."""

        return 1

    def poly_plot(plotfile, fill):
        """Convert polygon file to graphics format and plot."""
        # Use mangle to generate graphics format file
        #plotfile = "mangle_graphics.dat"
        #cmd = "/research/astro/gama/loveday/sw/mangle2.2/bin/poly2poly"
        #args = [cmd, "-og{}".format(res), polyfile, plotfile]
        #print (args)
        #subprocess.check_call(args)

        f = open(plotfile, 'r')
        line = f.readline()
        npoly = int(line.split()[0])
        line = f.readline()  # skip units line
        id = np.zeros(npoly, dtype=np.int32)
        weight = np.zeros(npoly)
        xcen = np.zeros(npoly)
        ycen = np.zeros(npoly)

        for ipoly in tqdm(range(npoly)):
            args = f.readline().split()
            id[ipoly] = int(args[1])
            npts = int(args[3])
            weight[ipoly] = float(args[7])
            xcen[ipoly] = float(args[9])
            ycen[ipoly] = float(args[10])

            ncsum = 0
            while (ncsum < npts):
                args = f.readline().split()
                nc = int(len(args)/2)
                x = np.zeros(int(nc+1))
                y = np.zeros(int(nc+1))
                for i in range(nc):
                    x[i] = float(args[2*i])
                    y[i] = float(args[2*i + 1])
                # close the polygon
                x[nc] = float(args[0])
                y[nc] = float(args[1])

                iplot = ipanel(x[0])
                ax = axes[iplot]
                if (fill == 0):
                    ax.plot(x, y)
                if (fill == 1):
    #                ax.fill(x, y, str(1 - grey_max*weight[ipoly]))
    #                ax.fill(x, y, str(grey_max*weight[ipoly]), ec='none')
                    ax.fill(x, y, fc=cmap(grey_max*weight[ipoly]), ec='none')
                if (fill == 2):
                    ax.fill(x, y, 'k', ec='none')

                ncsum += nc
        
        #print (npoly, ' polygons read 2 from ', polyfile)
        f.close()

    plt.clf()
    ax1 = plt.subplot2grid((10,1), (0,0), rowspan=1)
    ax2 = plt.subplot2grid((10,1), (2,0), rowspan=8)
    ax2.set_xlim([157.25, 225.0])
    ax2.set_ylim([-3.95, 3.95])
    #ax2.set_facecolor('black')
    #ax3 = plt.subplot2grid((19,1), (8,0), rowspan=5)
    #ax4 = plt.subplot2grid((19,1), (14,0), rowspan=5)
    axes = [ax1, ax2] #ax3, ax4]
    cmap = matplotlib.cm.gray
    norm = mpl.colors.Normalize(vmin=0, vmax=1)
    cb1 = mpl.colorbar.ColorbarBase(ax1, cmap=cmap,
                                    norm=norm,
                                    orientation='horizontal')
    ax1.set_title('WAVES WIDE-N MASK')
    for iplot in ([1]):
        ax = axes[iplot]
#        ax.axis(limits[iplot - 1], 'scaled') - changes
#        lims = limits[iplot - 1]
#        ax.fill((lims[0], lims[1], lims[1], lims[0], lims[0]),
#                (lims[2], lims[2], lims[3], lims[3], lims[2]), 'k')
    
    ax.set_ylabel('Dec [degrees]')
    ax.set_xlabel('RA [degrees]')

#    plt.subplots_adjust(hspace=0.2)
#    cmap = matplotlib.cm.viridis
    fig = plt.gcf()
    print('Starting plotting main mask')
    poly_plot(plotfile, fill)
    
    print('Finished plotting main mask, moving to starmask')

    #poly_plot("gaia_mask.ply", 2) #Plot mask- Superceeds earlier masking definition
    poly_plot('starmask_n_reg_graphics.dat', 2)
    print('Finished plotting starmask, now plotting ghostmask')
    poly_plot('ghostmask_n_reg_graphics.dat', 2)
    print('Finished plotting ghostmask, now plotting ngc mask')
    poly_plot('ngc_n_reg_graphics.dat', 2)

    plt.draw()
    if plot_file:
        fig.set_size_inches(plot_size)
        plt.savefig(plot_file, bbox_inches='tight')
    exit()
