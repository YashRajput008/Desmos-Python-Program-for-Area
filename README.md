# Background
- For a Calc BC Project, I had to design a character in desmos using polar and parametric equations; and compute the total area of the figure. However, due to my graph having 300+ equations, I decided to write a python program that would use the downloadable PNG file that Desmos provides to determine the area of my shape. This project also uses @MathEnthusiast314's "export expressions from a graph" javascript code that can be found below:
- The program uses Image Thresholding(basically just turning a png image into white and black so that it's easier to separate sections) to determine the area in the shape.
- Keep in mind that this only works for one object at a time, so if you have multiple separated objects(like Gojo's hollow purple and Gojo's body) then you'll have to separate the images
- The Python libraries that you'll need for this project are: Shapely, Numpy, Matplotlib, Pillow, and SciPy

```javascript
state=Calc.getState();
download(new Date() + "\n" + state.expressions.list.map(x=>{
    y=JSON.stringify(x.latex);
    y=y ? y : '';
    return (y.substring(1, y.length - 1))
}).join('\n'), "expressions.txt", "text/plain; charset=UTF-8");

function download(data, filename, type) { // from https://github.com/SlimRunner/desmos-scripts-addons/blob/master/graph-archival-script/
    var file = new Blob([data], {
        type: type
    });
    if (window.navigator.msSaveOrOpenBlob) // IE10+
        window.navigator.msSaveOrOpenBlob(file, filename);
    else { // Others
        var a = document.createElement("a"),
            url = URL.createObjectURL(file);
        a.href = url;
        a.download = filename;
        document.body.appendChild(a);
        a.click();
        setTimeout(function() {
            document.body.removeChild(a);
            window.URL.revokeObjectURL(url);
        }, 0);
    }
}
```
<hl>

## Example Images of Program
<img width="1202" height="475" alt="Matplotlib Visual Data Analysis" src="https://github.com/user-attachments/assets/dd494373-f4ac-4a87-8973-1b37096e2a09" />
<figcaption>This is the Matplotlib Visual Data Analysis showing the section that was calculated by the program</figcaption>

<br>
<br>
<br>

<img width="1196" height="471" alt="image" src="https://github.com/user-attachments/assets/57c1610d-21df-4cfa-bfd3-82ee5237bf41" />
<figcaption>This is the same image as above, just with the majority of the whitespace removed from the program to give a more accurate answer for the area</figcaption>

<br>
<br>
<br>


<img width="219" height="405" alt="{4453C9D7-D6E0-42D4-A139-CF7E18589AC4}" src="https://github.com/user-attachments/assets/c7560ee6-33df-4a00-8b68-5976889eeee7" />
<newline>
<figcaption>For reference, this is the original desmos graph</figcaption>
