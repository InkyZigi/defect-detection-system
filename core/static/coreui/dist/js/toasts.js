/* global coreui */

/**
 * --------------------------------------------------------------------------
 * CoreUI Free Boostrap Admin Template (v4.2.2): popovers.js
 * Licensed under MIT (https://coreui.io/license)
 * --------------------------------------------------------------------------
 */

const toastTrigger = document.getElementById('liveToastBtn');
const toastLive = document.getElementById('liveToast');
if (toastTrigger) {
  toastTrigger.addEventListener('click', () => {
    const toast = new coreui.Toast(toastLive);
    toast.show();
  });
}
//# sourceMappingURL=toasts.js.map
