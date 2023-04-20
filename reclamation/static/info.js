let info=document.getElementById("info");
let button=document.getElementById("button_hide")
button.addEventListener('click',show);
function show(){;
    if(info.className==="hide"){
        info.className="show";
    }
    else{info.className='hide';}
}