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

/*
 * Function to open Recent Activity
 * links on mobile devices
 */


function openActivity() {
    let activity = document.getElementById("activity-thread");
    activity.style.display = 'flex';
    activity.style.flexDirection = 'column';
    activity.style.flexWrap = 'nowrap';
    activity.style.height = '80%'
    activity.style.width = '80%';
    activity.style.position = 'fixed';
    activity.style.backgroundColor = 'blue';
    activity.style.alignContent = 'center';
    activity.style.left = '50%';
    activity.style.top = '50%';
    activity.style.transform = 'translate(-50%, -50%)';
    activity.style.zIndex = '10';
    console.log("test");
    }

