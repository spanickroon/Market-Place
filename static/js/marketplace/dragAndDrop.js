var dropArea = document.getElementById('drop-area');
dropArea.addEventListener('drop', handleDrop, false);

function dropHandler(ev) {
    ev.preventDefault();
}

function dragOverHandler(ev) {
    ev.preventDefault();
}

function handleDrop(e) {
    let dt = e.dataTransfer;
    let files = dt.files;

    handleFiles(files);
  }

function handleFiles(files) {
    files = [...files];
    files.forEach(previewFile);
  }

function previewFile(file) {
    let reader = new FileReader();
    
    if (file.type.includes('image')) {
        reader.readAsDataURL(file);
    
        reader.onloadend = function() {
            let img = document.createElement('img');
            img.src = reader.result;

            let newImg = document.getElementById('new-img-profile')

            newImg.innerHTML = "";
            newImg.appendChild(img);
        }
    }
}
