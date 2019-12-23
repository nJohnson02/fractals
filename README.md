# Fractals
![](https://img.shields.io/badge/build-passing-green/?style=flat-square)
![](https://img.shields.io/github/repo-size/Dapp3rDuck/fractals?style=flat-square)
![](https://img.shields.io/github/issues/Dapp3rDuck/fractals?style=flat-square)
![](https://img.shields.io/github/v/release/Dapp3rDuck/fractals?include_prereleases&style=flat-square)

* This script will prompt for in input of a fractal algorithym of the form `z = z**n + c`.
* c is the independent complex variable, and z is the dependent variable, changed after each iteration.
* I would suggest using the fractal z = z**2 + c with a resolution of 500x500 pixels, domain of [-2, 2], range of [-2, 2] and 1000 iterations for your first try.
* More iterations make the image more accurate, but take longer to render. 1000 iterations is a good value if you're resolution isn't too crazy.
See some example renders in <a href="/Renders">/Renders</a><br/>
You can explore a render that took over 130 hours in 12500 x 25000 resolution at: http://www.livepond.net/sites/mandelbrot<br/>
The python modules: Pillow and NumPy are required for the python script.<br/>
I copy pasted some of the code.

## Getting Started

```
$ git clone git@github.com:Dapp3rDuck/fractals.git
$ pip install colorsys numpy Pillow
```
<br/><br/>
<img src="Renders/MEGA.png" width="100%" height="auto">

| <img src="Renders/EX4.png" width="200px" height="200px"> | <img src="Renders/EX2.png" width="200px" height="200px"> | <img src="Renders/EX3.png" width="200px" height="200px"> |
| :---: |:---:|:---:|

## Contributors
| <a href="https://github.com/Le-SirH" target="_blank">**Le-SirH**</a> | <a href="https://github.com/Dapp3rDuck" target="_blank">**Dapp3rDuck**</a> | <a href="https://github.com/RHarr6306" target="_blank">**RHarr6306**</a> |
| :---: |:---:|:---:|
|[![Le-SirH](https://avatars3.githubusercontent.com/u/46948579?s=460&v=4)](https://github.com/Le-SirH)|[![Dapp3rDuck](https://avatars1.githubusercontent.com/u/55905788?s=400&v=4)](https://github.com/Dapp3rDuck)|[![RHarr6306](https://avatars2.githubusercontent.com/u/55287042?s=460&v=4)](https://github.com/RHarr6306)|
