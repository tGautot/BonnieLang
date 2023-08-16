console.log("main")

var gridInput = document.getElementById("grid-input");

var l2s = {
    "AddToStack": "A2S",
    "PopStack": "PS",
    "PrintStr": "PrntS",
    "PrintInt": "PrntI",
    "PrintChr": "PrntC", 
    "Add": "+",
    "Sub": "-",
    "Mul": "x",
    "Div": "/",
    "Mod": "%",
    "JumpTo": "JT",
    "JumpFrw": "JF",
    "IfZeroJumpTo": "ZJT",
    "IfZeroJumpFrw": "ZJF",
    "IfZogJumpTo": "ZGJT",
    "IfZogJumpFrw": "ZGJF",
    "ReadChar": "Read",
    "Store": "Store",
    "None": ""
}

var l2col = {
    "AddToStack": "green",
    "PopStack": "red",
    "PrintStr": "purple",
    "PrintInt": "purple",
    "PrintChr": "purple", 
    "Add": "brown",
    "Sub": "brown",
    "Mul": "brown",
    "Div": "brown",
    "Mod": "brown",
    "JumpTo": "blue",
    "JumpFrw": "blue",
    "IfZeroJumpTo": "gold",
    "IfZeroJumpFrw": "gold",
    "IfZogJumpTo": "gold",
    "IfZogJumpFrw": "gold",
    "ReadChar": "Salmon",
    "Store": "rebeccapurple",
    "None": "grey"
}

var stage = new Konva.Stage({
    container: 'container',   // id of container <div>
    width: 0,
    height: 0
});
var layer = new Konva.Layer();
// add the layer to the stage
stage.add(layer);

var grid = []
var cols = 0;
var rows = 0;

function parseGrid(){
    let all = gridInput.value;
    let lines = all.split("\n");
    
    grid = []
    let longestLine = -1;
    for(let i = 0; i < lines.length; i++){
        grid.push(lines[i].split(","))
        for(let j = 0; j < grid[i].length; j++){
            grid[i][j] = grid[i][j].trim()
        }
        longestLine = Math.max(longestLine, grid[i].length);
    }
    cols = longestLine;
    rows = grid.length;

    for(let i = 0; i < rows; i++){
        for(let j = 0; j < cols; j++){
            if(j >= grid[i].length){
                grid[i].push("0")
            }
        }
    }

}

function gridToStr(){
    return grid.map(l=>l.join(",")).join("\n")
}


function render(){
    parseGrid()
    
    console.log("Rendering ")
    console.log(grid);
    
    let pixPerSqr = 50;
    
    layer.destroyChildren();
    stage.width(pixPerSqr*cols);
    stage.height(pixPerSqr*rows);

    
    for(let i = 0; i < grid.length; i++){
        for(let j = 0; j < grid[i].length; j++){
            let elem, col, txt;
            elem = grid[i][j];
            col = l2col[elem];
            if(!col){col = "white";}
            txt = l2s[elem];
            if(!txt){txt = "";}
            
            // create our shape
            let sqr = new Konva.Rect({
                x: pixPerSqr*j,
                y: pixPerSqr*i,
                width: pixPerSqr,
                height: pixPerSqr,
                fill: col,
                stroke: 'black',
                strokeWidth: 2
            });

            let fontSz = 16;
            let inTxt = new Konva.Text({
                x: pixPerSqr*j,
                y: pixPerSqr*i+(pixPerSqr-fontSz)/2,
                width: pixPerSqr,
                fill: "white",
                align: "center",
                text: txt,
                fontSize: fontSz,
                fontStyle: "bold",
                // Used in event listener
                name: i + "-" + j
            })

            function onGridSqrClick(){
                let sqrNewJob = getSelectedButton();
                console.log(grid, i, j, this);
                grid[i][j] = sqrNewJob;
                gridInput.value = gridToStr();
                render();
            }
            function onTxtSqrClick(){
                // Konva doesnt bubble event between objects, need to do it ourself
                console.log("Clicked on text at ",i,j);
                onGridSqrClick()
            
            }

            sqr.on("click", onGridSqrClick);
            inTxt.on("click", onTxtSqrClick)

            // add the shape to the layer
            layer.add(sqr);
            layer.add(inTxt);
            
            
        }
    }

    
    
    
    // draw the image
    layer.draw();
}

function extend(way){
    let init = gridInput.value;
    if(way == "up"){
        let toInsert = Array.from({length: cols}, (v,i)=>'0').join(",");
        gridInput.value = toInsert + "\n" + init;
    }
    if(way == "down"){
        let toInsert = Array.from({length: cols}, (v,i)=>'0').join(",");
        let toJoin = init.split("\n").filter(v=>v!=="").join('\n');
        gridInput.value = init + "\n" + toInsert;
    }
    if(way == "left"){
        gridInput.value = init.split("\n").filter(v=>v!=="").map(v=>"0,"+v).join("\n")
    }
    if(way == "right"){
        gridInput.value = init.split("\n").filter(v=>v!=="").map(v=>v+",0").join("\n")
    }
    render()
}

function trimBorders(){
    while(grid[0].every(v=>!l2s[v])){
        grid.splice(0,1)
    }
    while(grid[grid.length-1].every(v=>!l2s[v])){
        grid.splice(grid.length-1,1)
    }
    while(grid.every(v=>!l2s[v[0]])){
        grid = grid.map(l=>l.slice(1))
    }
    while(grid.every(v=>!l2s[v[v.length-1]])){
        grid = grid.map(l=>l.slice(0,-1))
    }
    gridInput.value = gridToStr();
    render();
}

function getSelectedButton(){
    let btns = document.getElementsByName("rb_grid_square");
    for(let i = 0; i < btns.length; i++){
        if(btns[i].checked){
            return btns[i].value;
        }
    }
}