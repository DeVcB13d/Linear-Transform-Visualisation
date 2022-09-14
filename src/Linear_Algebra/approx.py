def approx(c):
    if c>0:
      ax=int(c*1000)
      cx=ax/10
      rx=round(cx)
      ix=rx/100
      print(ix)
    if c<0:
      ay=int(c*-1000)
      cy1=int(ay/100)
      ay1=ay-(cy1*100)
      cy=int(ay1/10)
      cy=ay1-(cy*10)
      cy2=0.01*cy
      ry=cy2
      sy1=0.1+ry
      sy1=sy1*100
      hy=ay-sy1+10
      iy=hy/1000
      iy=-iy
      print(iy)
x1=float(input("Enter x coordinate:"))
y1=float(input("Enter y coordinate:"))
approx(x1)
approx(y1)
