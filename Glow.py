# https://www.shadertoy.com/view/stdGzH

import taichi as ti
ti.init()

res_x = 1024
res_y = 576

pixels = ti.Vector.field(3, ti.f32)
ti.root.dense(ti.i, res_x).dense(ti.j, res_y).place(pixels)

@ti.kernel
def render(t :ti.f32):
    for i, j in pixels:
        color = ti.Vector([0.0, 0.0, 0.0])
        uv = ti.Vector([float(i) / res_x, float(j) / res_y])
        mag = 100.0
        uv*=10.0
        uv[1]-=5.0
        uv[1]+=ti.cos(uv[1] + t) * ti.sin(uv[0] + t) * ti.sin(uv[0] + t)
        mag = ti.abs(4.0/(20.0 * uv[1]))
        color = ti.Vector([mag, mag, mag])
        pixels[i, j] = color

gui = ti.GUI("Glow", res=(res_x, res_y))
for i in range(50000):
    t = i*0.03
    render(t)
    gui.set_image(pixels)
    gui.show()