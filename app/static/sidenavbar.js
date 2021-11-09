var mini = true;
function toggleNavbar() {
    if (mini) {
        console.log("opening sidebar");
        document.getElementById("navbar").style.width = "300px";
        document.getElementById("content").style.marginLeft = "10%";
        this.mini = false;
    } else {
        console.log("closing sidebar");
        document.getElementById("navbar").style.width = "5%";
        document.getElementById("content").style.marginLeft = "5%";
        this.mini = true;
    }
}