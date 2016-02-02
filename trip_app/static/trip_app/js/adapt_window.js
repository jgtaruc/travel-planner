function resize_elements() {
  if(window.innerWidth < window.innerHeight) {
    document.getElementById('bg').style.top = "56%";
  }
  else {
    document.getElementById('bg').style.top = "0px";
  }
}
