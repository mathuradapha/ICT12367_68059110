const textarea = document.getElementById("feedback");
const counter = document.getElementById("charCount");
const progressBar = document.getElementById("progressBar");
const maxLength = 100;

textarea.addEventListener("input", function(){
    let length = textarea.value.length;
    counter.textContent = length;

    let percent = (length / maxLength) * 100;
    progressBar.style.width = percent + "%";

    // เปลี่ยนสีเมื่อใกล้เต็ม
    if(length >= 80){
        progressBar.style.background = "red";
        counter.style.color = "red";
    }else{
        progressBar.style.background = "#0d6efd";
        counter.style.color = "#000";
    }
});