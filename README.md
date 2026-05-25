# Background
- For my Calc BC Final Project, I had to design a character in desmos using polar and parametric equations; and compute the total area of the entire shape as well as the perimeter of the figure. However, due to my graph having 300+ equations, I decided to write a python program that would use the downloadable SVG file that Desmos provides to determine the area and perimeter of my shape. This project also uses @MathEnthusiast314's "export expressions from a graph" javascript code that can be found below:

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
