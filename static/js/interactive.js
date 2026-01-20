// Enhanced Interactive Features for Inventory Management System

// Initialize on Document Ready
document.addEventListener('DOMContentLoaded', function() {
  initializeTooltips();
  initializeFormValidation();
  initializeTableFeatures();
  initializeAnimations();
});

// ====== Tooltips ======
function initializeTooltips() {
  const elements = document.querySelectorAll('[data-tooltip]');
  elements.forEach(el => {
    el.addEventListener('mouseenter', showTooltip);
    el.addEventListener('mouseleave', hideTooltip);
  });
}

function showTooltip(e) {
  const tooltip = document.createElement('div');
  tooltip.className = 'tooltip-box';
  tooltip.textContent = e.target.getAttribute('data-tooltip');
  tooltip.style.position = 'absolute';
  tooltip.style.backgroundColor = '#2563eb';
  tooltip.style.color = 'white';
  tooltip.style.padding = '0.5rem 0.75rem';
  tooltip.style.borderRadius = '6px';
  tooltip.style.fontSize = '0.875rem';
  tooltip.style.zIndex = '1000';
  tooltip.style.whiteSpace = 'nowrap';
  document.body.appendChild(tooltip);
  
  const rect = e.target.getBoundingClientRect();
  tooltip.style.top = (rect.top - tooltip.offsetHeight - 10) + 'px';
  tooltip.style.left = (rect.left + rect.width / 2 - tooltip.offsetWidth / 2) + 'px';
}

function hideTooltip() {
  const tooltip = document.querySelector('.tooltip-box');
  if (tooltip) tooltip.remove();
}

// ====== Form Validation ======
function initializeFormValidation() {
  const forms = document.querySelectorAll('form');
  forms.forEach(form => {
    form.addEventListener('submit', validateForm);
  });
  
  const inputs = document.querySelectorAll('input, textarea, select');
  inputs.forEach(input => {
    input.addEventListener('blur', validateField);
    input.addEventListener('focus', clearFieldError);
  });
}

function validateForm(e) {
  let isValid = true;
  const form = e.target;
  const requiredFields = form.querySelectorAll('[required]');
  
  requiredFields.forEach(field => {
    if (!field.value.trim()) {
      showFieldError(field, 'This field is required');
      isValid = false;
    }
  });
  
  if (!isValid) {
    e.preventDefault();
    showAlert('Please fill all required fields', 'danger');
  }
}

function validateField(e) {
  const field = e.target;
  if (field.hasAttribute('required') && !field.value.trim()) {
    showFieldError(field, 'This field is required');
  } else if (field.type === 'email' && field.value && !isValidEmail(field.value)) {
    showFieldError(field, 'Please enter a valid email');
  } else if (field.type === 'number' && field.value && isNaN(field.value)) {
    showFieldError(field, 'Please enter a valid number');
  } else {
    clearFieldError(e);
  }
}

function showFieldError(field, message) {
  field.classList.add('is-invalid');
  let errorMsg = field.parentElement.querySelector('.field-error');
  if (!errorMsg) {
    errorMsg = document.createElement('div');
    errorMsg.className = 'field-error';
    errorMsg.style.color = '#ef4444';
    errorMsg.style.fontSize = '0.875rem';
    errorMsg.style.marginTop = '0.25rem';
    field.parentElement.appendChild(errorMsg);
  }
  errorMsg.textContent = message;
}

function clearFieldError(e) {
  const field = e.target;
  field.classList.remove('is-invalid');
  const errorMsg = field.parentElement.querySelector('.field-error');
  if (errorMsg) errorMsg.remove();
}

function isValidEmail(email) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

// ====== Table Features ======
function initializeTableFeatures() {
  const tables = document.querySelectorAll('.table');
  tables.forEach(table => {
    addTableRowHover(table);
    addTableSorting(table);
  });
}

function addTableRowHover(table) {
  const rows = table.querySelectorAll('tbody tr');
  rows.forEach(row => {
    row.addEventListener('mouseenter', function() {
      this.style.backgroundColor = '#f0f9ff';
    });
    row.addEventListener('mouseleave', function() {
      this.style.backgroundColor = '';
    });
  });
}

function addTableSorting(table) {
  const headers = table.querySelectorAll('thead th');
  headers.forEach((header, index) => {
    header.style.cursor = 'pointer';
    header.addEventListener('click', function() {
      sortTable(table, index);
    });
  });
}

function sortTable(table, columnIndex) {
  const rows = Array.from(table.querySelectorAll('tbody tr'));
  const isAscending = !table.getAttribute('data-sort-asc');
  
  rows.sort((a, b) => {
    const aValue = a.cells[columnIndex].textContent;
    const bValue = b.cells[columnIndex].textContent;
    
    if (!isNaN(aValue) && !isNaN(bValue)) {
      return isAscending ? aValue - bValue : bValue - aValue;
    }
    return isAscending ? aValue.localeCompare(bValue) : bValue.localeCompare(aValue);
  });
  
  const tbody = table.querySelector('tbody');
  rows.forEach(row => tbody.appendChild(row));
  
  table.setAttribute('data-sort-asc', isAscending ? 'false' : 'true');
}

// ====== Alerts & Notifications ======
function showAlert(message, type = 'info') {
  const alert = document.createElement('div');
  alert.className = `alert alert-${type}`;
  alert.innerHTML = `
    <div style="display: flex; justify-content: space-between; align-items: center;">
      <span>${message}</span>
      <button type="button" style="background: none; border: none; cursor: pointer; font-size: 1.25rem;">&times;</button>
    </div>
  `;
  
  alert.style.position = 'fixed';
  alert.style.top = '80px';
  alert.style.right = '20px';
  alert.style.zIndex = '9999';
  alert.style.minWidth = '300px';
  alert.style.animation = 'slideIn 0.3s ease';
  
  document.body.appendChild(alert);
  
  const closeBtn = alert.querySelector('button');
  closeBtn.addEventListener('click', function() {
    alert.style.animation = 'slideOut 0.3s ease';
    setTimeout(() => alert.remove(), 300);
  });
  
  setTimeout(() => {
    if (alert.parentElement) {
      alert.style.animation = 'slideOut 0.3s ease';
      setTimeout(() => alert.remove(), 300);
    }
  }, 5000);
}

// ====== Animations ======
function initializeAnimations() {
  const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  };
  
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.animation = 'slideUp 0.5s ease forwards';
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);
  
  document.querySelectorAll('.card, .form-section, .table-responsive').forEach(el => {
    observer.observe(el);
  });
}

// ====== Loading State ======
function showLoadingState(button) {
  button.disabled = true;
  button.innerHTML = '<span class="spinner"></span> Loading...';
}

function hideLoadingState(button, text) {
  button.disabled = false;
  button.innerHTML = text;
}

// ====== Export Functions ======
function exportTableToCSV(tableId, filename) {
  const table = document.getElementById(tableId);
  if (!table) return;
  
  let csv = [];
  const rows = table.querySelectorAll('tr');
  
  rows.forEach(row => {
    const cols = row.querySelectorAll('td, th');
    let csvRow = [];
    cols.forEach(col => {
      csvRow.push('"' + col.textContent + '"');
    });
    csv.push(csvRow.join(','));
  });
  
  downloadFile(csv.join('\n'), filename + '.csv', 'text/csv');
}

function exportTableToExcel(tableId, filename) {
  const table = document.getElementById(tableId);
  if (!table) return;
  
  const html = '<html><head><meta charset="UTF-8"></head><body>' + table.outerHTML + '</body></html>';
  downloadFile(html, filename + '.xls', 'application/msexcel');
}

function downloadFile(content, filename, type) {
  const element = document.createElement('a');
  element.setAttribute('href', 'data:' + type + ';charset=utf-8,' + encodeURIComponent(content));
  element.setAttribute('download', filename);
  element.style.display = 'none';
  document.body.appendChild(element);
  element.click();
  document.body.removeChild(element);
}

// ====== Print Function ======
function printTable(tableId) {
  const table = document.getElementById(tableId);
  if (!table) return;
  
  const printWindow = window.open('', '', 'height=600,width=800');
  printWindow.document.write('<html><head><title>Print</title>');
  printWindow.document.write('<link rel="stylesheet" href="/static/css/bootstrap.min.css">');
  printWindow.document.write('<link rel="stylesheet" href="/static/css/main.css">');
  printWindow.document.write('<link rel="stylesheet" href="/static/css/modern.css">');
  printWindow.document.write('</head><body>');
  printWindow.document.write(table.outerHTML);
  printWindow.document.write('</body></html>');
  printWindow.document.close();
  printWindow.print();
}

// ====== Search with Highlighting ======
function searchWithHighlight(inputId, tableId) {
  const input = document.getElementById(inputId);
  const table = document.getElementById(tableId);
  
  if (!input || !table) return;
  
  input.addEventListener('keyup', function() {
    const filter = this.value.toUpperCase();
    const rows = table.querySelectorAll('tbody tr');
    
    rows.forEach(row => {
      let found = false;
      const cells = row.querySelectorAll('td');
      
      cells.forEach(cell => {
        const text = cell.textContent.toUpperCase();
        if (text.includes(filter)) {
          found = true;
          cell.innerHTML = cell.textContent.replace(new RegExp(filter, 'g'), '<mark style="background-color: #fef3c7;">' + filter + '</mark>');
        } else {
          cell.innerHTML = cell.textContent;
        }
      });
      
      row.style.display = found || filter === '' ? '' : 'none';
    });
  });
}

// ====== Add CSS Styles Dynamically ======
function addDynamicStyles() {
  const style = document.createElement('style');
  style.textContent = `
    .is-invalid {
      border-color: #ef4444 !important;
      box-shadow: 0 0 0 3px rgba(239, 68, 68, 0.1) !important;
    }
    
    .field-error {
      color: #ef4444;
      font-size: 0.875rem;
      margin-top: 0.25rem;
      display: block;
    }
    
    mark {
      background-color: #fef3c7;
      padding: 0.2rem 0.4rem;
      border-radius: 3px;
    }
    
    @keyframes slideOut {
      from {
        opacity: 1;
        transform: translateX(0);
      }
      to {
        opacity: 0;
        transform: translateX(400px);
      }
    }
  `;
  document.head.appendChild(style);
}

// Initialize dynamic styles
addDynamicStyles();

// Export for use in other files
window.InventoryApp = {
  showAlert,
  showLoadingState,
  hideLoadingState,
  exportTableToCSV,
  exportTableToExcel,
  printTable,
  searchWithHighlight,
  validateField
};
