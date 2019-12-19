# Fractals
* This script will prompt for in input of a fractal algorithym of the form z = z**n + c.
* c is the independent complex variable, and z is the dependent variable, changed after each iteration.
* I would suggest using the fractal z = z**2 + c with a resolution of 500x500 pixels, domain of [-2, 2], range of [-2, 2] and 1000 iterations for your first try.
* More iterations make the image more accurate, but take longer to render. 1000 iterations is a good value if your're resolution isn't too crazy.
<br/><br/>
See some example renders in <a href="/Renders">/Renders</a>
<br/><br/>
You can explore a render that took over 130 hours in 12500 x 25000 resolution at: http://www.livepond.net/sites/mandelbrot
<br/><br/>
The python modules: Pillow and NumPy are required for the python script.
<br/><br/>
I copy pasted some of the code, so yeah.
<br/><br/>
<img src="Renders/MEGA.png" width="600px" height="300px">
<table>
  <tr>
    <td><img src="Renders/EX1.png" width="300px" height="300px"></td>
    <td><img src="Renders/EX2.png" width="300px" height="300px"></td>
    <td><img src="Renders/EX3.png" width="300px" height="300px"></td>
  </tr>
</table>
