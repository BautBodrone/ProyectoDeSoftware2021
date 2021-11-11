var mini = true;
function toggleNavbar() {
    if (mini) {
        console.log("opening sidebar");
        document.getElementById("navbar").style.width = "300px";
        this.mini = false;
    } else {
        console.log("closing sidebar");
        document.getElementById("navbar").style.width = "15%";
        this.mini = true;
    }
}
