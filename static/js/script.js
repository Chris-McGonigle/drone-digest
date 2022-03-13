/*
 * Function to open Browse Subject
 * links on mobile devices
 */


function openBrowse() {
    let browse = document.getElementById("subject-filter");
    browse.style.display = 'flex';
    browse.style.flexDirection = 'column';
    browse.style.flexWrap = 'wrap';
    browse.style.width = '80%';
    browse.style.position = 'fixed';
    browse.style.backgroundColor = 'blue';
    browse.style.alignContent = 'center';
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
    close.style.display = 'none'
}
