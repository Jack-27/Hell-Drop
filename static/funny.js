for (let i = 1; i < 262; i++) {
    let sue =  document.createElement("p")
    sue.setAttribute("id", `fuck${i}`)
    sue.setAttribute("class", "Haha")
    sue.innerHTML = "sue me &nbsp;"
    document.getElementById("ohLord").appendChild(sue)
    console.log("kms")
 }
 function hide(id) {
     let sue = document.getElementById(`fuck${id}`)
     if (sue.style.opacity == "0") {
         sue.style.opacity = "1"
     } else {
         sue.style.opacity = "0"
     }
 }

 document.getElementById("ohLord").onclick  = function() {
     console.log("huhj")
     for (let a = 1; a < 262; a++) {
         if ([5,14,23,32,41,50,59,68,77,86,95,103,105,104,113,112,114,111,122,121,123,120,257,256,2568,248,247,246,249,250,239,240,241,238,237,228,229,230,231,232,219,220,221,222,223,210,196,187,211,212,213,215,258,201,202,203,204,206,192,193,194,195,197,183,184,185,186,188,214,156,157,158,159,131,132,129,130,140,139,138,141,149,150,148,147,176,175,174,177,179,167,166,165,168,170,205,161,152].includes(a)) {
             
             console.log("this isnt fun anymore oh god please help me")
         } else {
            hide(a)
         }
     }
 }