import tkinter as tk

class MandelbrotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mandelbrot Set Explorer")
        
        self.width = 600
        self.height = 600
        
        self.canvas = tk.Canvas(root, width=self.width, height=self.height, bg="black")
        self.canvas.pack()
        
        self.draw_mandelbrot()

    def mandelbrot(self, c, max_iter):
        z = 0.0j
        for i in range(max_iter):
            if z.real*z.real + z.imag*z.imag > 4.0:
                return i
            z = z*z + c
        return max_iter

    def draw_mandelbrot(self):
        img = tk.PhotoImage(width=self.width, height=self.height)
        self.canvas.create_image((0, 0), image=img, anchor="nw")
        
        x_min, x_max = -2.0, 0.5
        y_min, y_max = -1.25, 1.25
        max_iter = 100
        
        for x in range(self.width):
            for y in range(self.height):
                zx = x_min + (x / self.width) * (x_max - x_min)
                zy = y_min + (y / self.height) * (y_max - y_min)
                c = complex(zx, zy)
                
                color_val = self.mandelbrot(c, max_iter)
                
                if color_val == max_iter:
                    color = "#000000"
                else:
                    shade = int(255 * color_val / max_iter)
                    color = f"#{shade:02x}{(shade * 3) % 255:02x}{255 - shade:02x}"
                
                img.put(color, (x, y))
        
        self.image_ref = img

if __name__ == "__main__":
    root = tk.Tk()
    app = MandelbrotApp(root)
    root.mainloop()
