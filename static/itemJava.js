function newSlidey(numOfPics, numOfColors) {
    let divslide = document.createElement("div");
    divslide.setAttribute("class", "itemSlide");
    document.getElementById("itemMain").appendChild(divslide);
    let mainimg = document.createElement("img")
    mainimg.src = document.getElementById('img10').src
    mainimg.setAttribute("class", "itemPic")
    mainimg.setAttribute("id", "mainImg")
    document.getElementById("itemMain").appendChild(mainimg);
    if (numOfPics == 1) {
        document.getElementById("itemMain").style.height = '534px'
    }
    for (let i = 1; i <= numOfColors; i++) {
        for (let j = 0; j < numOfPics; j++) {
            let img = document.createElement('img');
            img.src = document.getElementById(`img${i * 10 + j}`).src
            img.setAttribute("class", "slide");
            img.setAttribute("id", `rlimg${i * 10 + j}`);
            img.style.borderRadius = "5%";
            img.style.height = "58px";
            img.style.width = `58px`
            img.style.borderRadius = '4px'
            img.style.borderColor = '#000000'
            img.style.borderStyle = 'solid'
            divslide.appendChild(img)
            img.style.display = 'none';
        }
    }
}

function reset(img) {
    img.style.borderColor = '#000000'
}

let imgNum = 0
for (i = 0; i < 4; i++) {
    if (document.getElementById(`img${i + 10}`)) {
        imgNum++
    }
}
let colorNum = 0
for (i = 1; i < 5; i++) {
    if (document.getElementById(`color${i}`)) {
        colorNum++
    }
}





function preVarChange() {
    if (imgNum >= 1){
       img0.onclick = ""
       img0.style.display = "none"
    }
    if (imgNum >= 2){
        img1.onclick = ""
        img1.style.display = "none"
    }
    if (imgNum >= 3){
        img2.onclick = ""
        img2.style.display = "none"
    }
    if (imgNum >= 4){
        img3.onclick = ""
        img3.style.display = "none"
    }
}
function postVarChange() {
    if (imgNum >= 1){
       img0.onclick = img0OnClick.bind()
       img0.style.display = "inline-block"
    }
    if (imgNum >= 2){
        img1.onclick = img1OnClick.bind()
        img1.style.display = "inline-block"
    }
    if (imgNum >= 3){
        img2.onclick = img2OnClick.bind()
        img2.style.display = "inline-block"
    }
    if (imgNum >= 4){
        img3.onclick = img3OnClick.bind()
        img3.style.display = "inline-block"
    }
}


if (document.getElementById("color1")) {
    document.getElementById("color1").onclick = function() {
        preVarChange()
        img0 = document.getElementById("rlimg10") 
        img1 = document.getElementById("rlimg11")
        img2 = document.getElementById("rlimg12")
        img3 = document.getElementById("rlimg13")
        postVarChange()
        img0OnClick()
    }
}
if (document.getElementById("color2")) {
    document.getElementById("color2").onclick = function() {
        preVarChange()
        img0 = document.getElementById("rlimg20") 
        img1 = document.getElementById("rlimg21")
        img2 = document.getElementById("rlimg22")
        img3 = document.getElementById("rlimg23")
        postVarChange()
        img0OnClick()
    }
}

if (document.getElementById("color3")) {
    document.getElementById("color3").onclick = function() {
        preVarChange()
        img0 = document.getElementById("rlimg30") 
        img1 = document.getElementById("rlimg31")
        img2 = document.getElementById("rlimg32")
        img3 = document.getElementById("rlimg33")
        postVarChange()
        img0OnClick()
    }
}

if (document.getElementById("color4")) {
    document.getElementById("color4").onclick = function() {
        preVarChange()
        img0 = document.getElementById("rlimg40") 
        img1 = document.getElementById("rlimg41")
        img2 = document.getElementById("rlimg42")
        img3 = document.getElementById("rlimg43")
        postVarChange()
        img0OnClick()
    }
}

newSlidey(imgNum, colorNum)

let mainimg = document.getElementById('mainImg')
let img0 = document.getElementById("rlimg10") 
let img1 = document.getElementById("rlimg11")
let img2 = document.getElementById("rlimg12")
let img3 = document.getElementById("rlimg13")
postVarChange()
let lastimg = img0
img0.style.borderColor = '#808080'

function img0OnClick() {
    mainimg.src = img0.src;
    img0.opacity = .5
    img0.style.borderColor = '#808080'  
    if (!(lastimg == img0))
    {
        reset(lastimg)
        lastimg = img0
    }
}
function img1OnClick() {
    mainimg.src = img1.src;
    img1.opacity = .5
    img1.style.borderColor = '#808080'   
    if (!(lastimg == img1))
    {
        reset(lastimg)
        lastimg = img1
    }
    
}
function img2OnClick() {
    img2.style.borderColor = '#808080'
    mainimg.src = img2.src;
    img2.opacity = .5
    if (!(lastimg == img2))
    {
        reset(lastimg)
        lastimg = img2
    }
}

function img3OnClick() {
    img3.style.borderColor = '#808080'
    mainimg.src = img3.src;
    img3.opacity = .5
    if (!(lastimg == img3))
    {
        reset(lastimg)
        lastimg = img3
    }
    
}