# gif_wall
A python script to combine multiple animated gifs into a single animated gif with some minor effects.

Usage:

>gif_wall.py control<br>

gif_wall is a script which expects to be run in the same directory as the source gifs and looks for a control file formatted as follows:

>quatermass_1.gif quatermass_2.gif quatermass_3.gif, green, h, 10<br>
>quatermass_1.gif quatermass_2.gif quatermass_3.gif, red, v, 10<br>


The final gif(s) will be created using the current epoch time with gif appended:

> 1486155335.gif<br>
> 1486155440.gif<br>

The format of the control file is as follows:

> gifname gifname gifname ..., color, orientation, gapsize<br>
> where color is something like black, red, green, etc.
> where orientation is "h" for horizontal and "v" for vertical.
> where gapsize is the space between gifs in pixels, i.e. 10 in the above example.

A results.gif is created for each iteration of the build process and removed once the n+1 gif has been added to the combined gif.  It is removed before the script exits.

Be aware that the final gif runs a long as the longest gif in the process.  I.E. if you have gifs that are 1s, 3s, and 5s in length, the final gif will run for 5s and the shorter length gifs will run to completion leaving behind the your color selection to fill in the extra time.  The gifs in the sample folder exhibit this effect.

Gifs in the sample folder were created by gif_grinder (https://github.com/dannen/gif_grinder)
