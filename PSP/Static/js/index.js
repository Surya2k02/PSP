function printTable() {
            var printContent = document.getElementById("printSection").innerHTML;
            var originalContent = document.body.innerHTML;

            document.body.innerHTML = printContent;
            window.print();
            document.body.innerHTML = originalContent;
            location.reload(); // ✅ Reload page after printing to restore buttons
        }

function updateDateTime() {
    const now = new Date();

    const options = {
        weekday: 'long',
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit'
    };

    const formattedDate = now.toLocaleDateString('en-US', options);
    document.getElementById("datetime").innerHTML = `📅 ${formattedDate}`;
}

// ✅ Call function on page load
window.onload = updateDateTime;


