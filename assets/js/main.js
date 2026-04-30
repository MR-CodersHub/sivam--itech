document.addEventListener('DOMContentLoaded', () => {
    // Initialize Lucide icons
    if (window.lucide) {
        lucide.createIcons();
    }

    // Handle Loader Dismissal
    window.addEventListener('load', () => {
        const loader = document.getElementById('loader');
        if (loader) {
            setTimeout(() => {
                loader.classList.add('loaded');
                setTimeout(() => {
                    loader.style.display = 'none';
                }, 500);
            }, 500);
        }
    });

    // Navbar Scroll Effect
    const nav = document.querySelector('nav');
    if (nav) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                nav.classList.add('scrolled');
            } else {
                nav.classList.remove('scrolled');
            }
        });
    }

    // Mobile Menu Toggle
    const menuButton = document.getElementById('mobile-menu-btn');
    if (menuButton) {
        menuButton.addEventListener('click', toggleMenu);
    }

    // Initialize Form Handlers
    initFormHandlers();
});

function toggleMenu() {
    const menu = document.getElementById('mobile-menu');
    if (menu) {
        menu.classList.toggle('active');
    }
}

// ✅ File Upload UI & Validation
function initFileUpload() {
    const resumeInput = document.getElementById("resume");
    const fileNameDisplay = document.getElementById("file-name");

    if (resumeInput && fileNameDisplay) {
        resumeInput.addEventListener('change', function (e) {
            const file = e.target.files[0];
            if (file) {
                const allowedExtensions = /(\.pdf|\.doc|\.docx)$/i;
                if (!allowedExtensions.exec(file.name)) {
                    alert('Invalid file type. Please upload a PDF or DOC file.');
                    this.value = '';
                    fileNameDisplay.textContent = 'Click to upload or drag and drop';
                    fileNameDisplay.classList.remove('text-brand-orange');
                    return;
                }
                if (file.size > 5 * 1024 * 1024) {
                    alert('File is too large. Maximum size is 5MB.');
                    this.value = '';
                    fileNameDisplay.textContent = 'Click to upload or drag and drop';
                    fileNameDisplay.classList.remove('text-brand-orange');
                    return;
                }
                fileNameDisplay.textContent = `Selected: ${file.name}`;
                fileNameDisplay.classList.add('text-brand-orange');
            } else {
                fileNameDisplay.textContent = 'Click to upload or drag and drop';
                fileNameDisplay.classList.remove('text-brand-orange');
            }
        });
    }
}

// ✅ Centralized Form Handling
function initFormHandlers() {
    const contactForm = document.getElementById("contactForm");
    const fileNameDisplay = document.getElementById("file-name");

    // Initialize file upload UI for careers page
    initFileUpload();

    if (contactForm) {
        // Prevent multiple listeners
        if (contactForm.dataset.listenerAttached) return;
        contactForm.dataset.listenerAttached = "true";

        contactForm.addEventListener("submit", async function (e) {
            e.preventDefault();

            const btn = document.getElementById("submit-btn") || this.querySelector('button[type="submit"]');
            const originalBtnText = btn ? btn.innerText : "Submit";

            if (btn) {
                btn.innerText = "Sending...";
                btn.disabled = true;
            }

            try {
                // Use FormData to correctly package files and fields
                // The input name attribute (resume) must match what Pabbly expects
                const formData = new FormData(this);

                // ✅ SEND TO PABBLY /filedata/ ENDPOINT
                // Do NOT manually set Content-Type header; fetch will set it with the correct boundary
                const response = await fetch("https://connect.pabbly.com/webhook-listener/filedata/IjU3NjIwNTY0MDYzNjA0MzY1MjZiNTUzMiI_3D_pc/IjU3NjcwNTZlMDYzNDA0MzA1MjZlNTUzYzUxM2Ei_pc", {
                    method: "POST",
                    body: formData
                });

                if (response.ok) {
                    // Show success modal if it exists
                    if (document.getElementById('success-modal')) {
                        showModal();
                    } else {
                        alert("Thank you! Your submission has been received successfully.");
                    }
                    
                    this.reset();
                    
                    // Reset file upload display
                    if (fileNameDisplay) {
                        fileNameDisplay.textContent = 'Click to upload or drag and drop';
                        fileNameDisplay.classList.remove('text-brand-orange');
                    }
                } else {
                    throw new Error("Server responded with an error");
                }

            } catch (error) {
                console.error("Submission Error:", error);
                alert("There was an error submitting the form. Please try again later.");
            } finally {
                if (btn) {
                    btn.innerText = originalBtnText;
                    btn.disabled = false;
                }
            }
        });
    }

    // Handle any other forms (Inquire, Newsletter, etc.)
    const allForms = document.querySelectorAll('form');
    allForms.forEach(form => {
        if (form.id !== 'contactForm' && !form.dataset.handled) {
            form.addEventListener('submit', (e) => {
                e.preventDefault();
                alert("Thank you! Your submission has been received.");
                form.reset();
                form.dataset.handled = "true";
            });
        }
    });
}

function showModal() {
    const modal = document.getElementById('success-modal');
    const content = document.getElementById('modal-content');
    if (modal && content) {
        modal.classList.remove('hidden');
        modal.classList.add('flex');
        setTimeout(() => {
            content.classList.remove('scale-95', 'opacity-0');
            content.classList.add('scale-100', 'opacity-100');
        }, 10);
    }
}

function closeModal() {
    const modal = document.getElementById('success-modal');
    const content = document.getElementById('modal-content');
    if (modal && content) {
        content.classList.remove('scale-100', 'opacity-100');
        content.classList.add('scale-95', 'opacity-0');
        setTimeout(() => {
            modal.classList.add('hidden');
            modal.classList.remove('flex');
        }, 300);
    }
}