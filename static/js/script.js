/*
 * Function to open Browse Subject
 * links on mobile devices
 */

var browse = document.getElementById("subject-filter");


function openBrowse() {
    browse.style.display = 'flex';
    browse.style.flexDirection = 'column';
    browse.style.flexWrap = 'wrap';
    browse.style.width = '80%';
    browse.style.position = 'fixed';
    browse.style.backgroundColor = '#364958';
    browse.style.alignContent = 'center';
    browse.style.border = '2px solid #ff5400';
    browse.style.borderRadius = '25px';
    browse.style.left = '50%';
    browse.style.top = '50%';
    browse.style.transform = 'translate(-50%, -50%)';
    browse.style.zIndex = '10';
    }


/*
 * Function to close Browse Subject
 * window when option selected
 */

function closeBrowse() {
    let close = document.getElementById("subject-filter");
    close.style.display = 'none';
}

