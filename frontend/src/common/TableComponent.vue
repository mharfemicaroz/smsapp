<template>
  <div
    v-if="!mainItems.length"
    class="d-flex justify-content-center align-items-center mt-3"
  >
    <div class="spinner-border" role="status">
      <span class="sr-only">Loading...</span>
    </div>
  </div>
  <div v-else>
    <div class="d-flex justify-content-between align-items-center mt-3 mb-2">
      <p class="mb-0 no-print">
        <label
          >Show
          <select
            v-model="rowsPerPage"
            aria-controls="example"
            style="height: 30px; font-size: medium"
          >
            <option value="10">10</option>
            <option value="25">25</option>
            <option value="50">50</option>
            <option value="100">100</option>
            <option value="999999">Show All</option>
          </select>
          entries</label
        >
        &NonBreakingSpace;
        <button class="btn btn-sm btn-primary" @click="printSection">
          <i class="fas fa-print"></i>
        </button>
        &nbsp;
        <button class="btn btn-sm btn-primary" @click="exportXLSX">
          <i class="fas fa-file-excel"></i>
        </button>
        &nbsp;
        <button class="btn btn-sm btn-primary" @click="saveAsPDF">
          <i class="fas fa-file-pdf"></i>
        </button>
      </p>
      <div class="form-outline col-md-3 mb-0 no-print">
        <input
          type="search"
          class="form-control"
          placeholder="Type query"
          v-model="searchText"
          aria-label="Search"
          autocomplete="off"
          aria-autocomplete="off"
        />
      </div>
    </div>

    <table
      class="table border-0 table-hover table-center mb-0 table-striped"
      v-bind:id="uniqueID"
    >
      <thead>
        <tr v-if="howmanyCheckbox > 0 && batchAction">
          <th :colspan="mainHeaders.length" style="border: 0px">
            <slot
              name="checkboxtrigger"
              :data="{
                dt: paginatedMainItems
                  .filter(function (item) {
                    return getItemsfromCheckedBoxes.includes(item.id);
                  })
                  .map(function (item) {
                    return item.id;
                  }),
              }"
            ></slot>
          </th>
        </tr>
        <tr>
          <template v-for="(header, index) in mainHeaders" :key="index">
            <th v-if="header.field === 'toggle' && toggleable">
              <button
                class="btn btn-sm btn-primary no-print"
                @click="toggleAll()"
              >
                <span v-if="showAll === false">+</span>
                <span v-else>-</span>
              </button>
            </th>
            <th v-else-if="header.field === 'checkbox' && selectable">
              <input
                type="checkbox"
                class="form-check-input no-print"
                @change="toggleCheckboxes"
                :value="mainCheckbox"
              />
            </th>
            <th
              v-else
              @click="sort(header.field)"
              :class="{ sortable: header.sortable }"
            >
              {{ header.label }}
              <span v-if="header.sortable" class="sort-icon no-print">
                <i
                  :class="[
                    'fas',
                    sortColumn === header.field && sortDirection === 1
                      ? 'fa-sort-alpha-up'
                      : 'fa-sort-alpha-down',
                  ]"
                ></i>
              </span>
            </th>
          </template>
        </tr>
      </thead>
      <tbody>
        <template
          v-for="(mainItem, mainIndex) in paginatedMainItems"
          :key="mainItem.id"
        >
          <tr :class="{ 'table-active': showTable[mainItem.id] }">
            <td
              v-for="(header, index) in mainHeaders"
              :key="index"
              :style="{
                wordWrap: 'break-word',
                whiteSpace: 'normal',
                overflow: 'hidden',
                maxWidth: '100%',
                textAlign: header.field === 'action' ? 'right' : 'left',
              }"
            >
              <template v-if="header.field === 'checkbox' && selectable">
                <input
                  type="checkbox"
                  class="mtCheckbox form-check-input no-print"
                  :data-id="mainItem.id"
                  @change="toggleCheckbox"
                />
              </template>
              <template v-else-if="header.field === 'toggle' && toggleable">
                <button
                  type="button"
                  @click="toggleTable(mainItem.id)"
                  class="btn btn-primary btn-sm toggle no-print"
                >
                  <span v-if="!showTable[mainItem.id]">+</span>
                  <span v-else>-</span>
                </button>
              </template>
              <template v-else-if="header.field === 'action'">
                <button
                  v-if="this.editable"
                  type="button"
                  class="btn btn-primary btn-sm no-print"
                  @click="$emit('edit-action', mainItem.id)"
                  style="margin-right: 10px"
                >
                  <i class="fas fa-edit"></i>
                </button>
                <button
                  v-if="this.custombtn"
                  type="button"
                  class="btn btn-primary btn-sm no-print"
                  @click="$emit('custombtn-action', mainItem.id)"
                >
                  <i class="fa fa-eye"></i>
                </button>
                <div v-if="moreAction">
                  <a
                    class="me-3 dropset"
                    data-bs-toggle="dropdown"
                    aria-expanded="false"
                    href="javascript:void(0);"
                    ><img src="/img/icons-ext/ellipise1.svg" alt="img"
                  /></a>
                  <ul
                    class="dropdown-menu"
                    aria-labelledby="dropdownMenuButton"
                    data-popper-placement="bottom-end"
                  >
                    <li v-for="(btn, index) of this.actionBtns">
                      <a
                        href="javascript:void(0);"
                        class="dropdown-item"
                        @click="$emit(`btn-action${index + 1}`, mainItem.id)"
                        >{{ btn }}</a
                      >
                    </li>
                  </ul>
                </div>
                <button
                  v-if="this.deletable"
                  type="button"
                  class="btn btn-danger btn-sm no-print"
                  @click="$emit('delete-action', mainItem.id)"
                >
                  <i class="fas fa-trash"></i>
                </button>
                <template v-if="header.slot" class="no-print">
                  <slot
                    name="custombtn"
                    :data="{ h: header.field, dt: mainItem }"
                  ></slot>
                </template>
              </template>
              <template v-else-if="header.field.toLowerCase().includes('date')">
                {{ formatDate(new Date(mainItem[header.field])) }}
              </template>
              <template v-else>
                <template v-if="header.slot">
                  <slot
                    name="content"
                    :data="{ h: header.field, dt: mainItem }"
                  ></slot>
                </template>
                <template v-else>
                  {{
                    typeof mainItem[header.field] === "object" &&
                    mainItem[header.field]
                      ? (Object.entries(mainItem[header.field]).find(
                          (entry) => entry[0] === header.identifier
                        ) || [null, null])[1]
                      : mainItem[header.field]
                  }}
                </template>
              </template>
            </td>
          </tr>
          <tr v-if="showTable[mainItem.id] && toggleable">
            <td :colspan="mainHeaders.length">
              <div v-if="slotsub" style="padding-left: 60px">
                <slot name="subcontent" :data="mainItem.items"></slot>
              </div>
              <div v-else style="padding-left: 60px">
                <div v-if="mainItem.items.length > 0">
                  <table
                    class="table"
                    style="table-layout: fixed; word-wrap: break-word"
                  >
                    <thead>
                      <tr>
                        <template
                          v-for="(subHeader, index) in subHeaders"
                          :key="index"
                        >
                          <th>{{ subHeader.label }}</th>
                        </template>
                      </tr>
                    </thead>
                    <tbody>
                      <template
                        v-for="(subItem, subIndex) in mainItem.items"
                        :key="subIndex"
                      >
                        <tr>
                          <template
                            v-for="(subHeader, index) in subHeaders"
                            :key="index"
                          >
                            <template v-if="subHeader.field.includes('date')">
                              <td>
                                {{
                                  formatDate(new Date(subItem[subHeader.field]))
                                }}
                              </td>
                            </template>
                            <template v-else>
                              <td>{{ subItem[subHeader.field] }}</td>
                            </template>
                          </template>
                        </tr>
                      </template>
                    </tbody>
                  </table>
                </div>
                <div v-if="mainItem.items2 && mainItem.items2.length > 0">
                  <table
                    class="table"
                    style="table-layout: fixed; word-wrap: break-word"
                  >
                    <thead>
                      <tr>
                        <template
                          v-for="(subHeader, index) in subHeaders2"
                          :key="index"
                        >
                          <th>{{ subHeader.label }}</th>
                        </template>
                      </tr>
                    </thead>
                    <tbody>
                      <template
                        v-for="(subItem, subIndex) in mainItem.items2"
                        :key="subIndex"
                      >
                        <tr>
                          <template
                            v-for="(subHeader, index) in subHeaders2"
                            :key="index"
                          >
                            <template v-if="subHeader.field.includes('date')">
                              <td>
                                {{
                                  formatDate(new Date(subItem[subHeader.field]))
                                }}
                              </td>
                            </template>
                            <template v-else>
                              <td>{{ subItem[subHeader.field] }}</td>
                            </template>
                          </template>
                        </tr>
                      </template>
                    </tbody>
                  </table>
                </div>
              </div>
            </td>
          </tr>
        </template>
        <tr>
          <td v-for="(header, index) in mainHeaders" :key="index">
            <span
              class="text-primary"
              v-if="header.reducible"
              style="font-weight: bold"
              >{{ sumColumn(header.field).toFixed(2) }}</span
            >
          </td>
        </tr>
      </tbody>
    </table>
    <div class="no-print">
      <nav aria-label="Table pagination">
        <div class="d-flex justify-content-between align-items-center mt-3">
          <p class="mb-0">
            Showing
            {{
              Math.min(
                (currentPage - 1) * rowsPerPage + 1,
                paginatedMainItems.length
              )
            }}
            to
            {{ Math.min(currentPage * rowsPerPage, paginatedMainItems.length) }}
            of {{ paginatedMainItems.length }} entries{{
              searchText
                ? " (filtered from " + mainItems.length + " total entries)"
                : ""
            }}
          </p>

          <ul class="pagination mb-0">
            <li class="page-item" :class="{ disabled: currentPage === 1 }">
              <button
                class="page-link btn-primary"
                @click="currentPage = 1"
                aria-label="First page"
              >
                <span aria-hidden="true">First</span>
              </button>
            </li>
            <li class="page-item" :class="{ disabled: currentPage === 1 }">
              <button
                class="page-link btn-primary"
                @click="currentPage -= 1"
                aria-label="Previous"
              >
                <span aria-hidden="true">Previous</span>
              </button>
            </li>
            <li
              v-for="pageNumber in visiblePages"
              :key="pageNumber"
              class="page-item"
              :class="{ active: currentPage === pageNumber }"
            >
              <button
                class="page-link btn-primary"
                @click="currentPage = pageNumber"
              >
                {{ pageNumber }}
              </button>
            </li>
            <li
              v-if="visiblePages[visiblePages.length - 1] < pageCount - 1"
              class="page-item disabled"
            >
              <span class="page-link">...</span>
            </li>
            <li
              class="page-item"
              :class="{ disabled: currentPage === pageCount }"
            >
              <button
                class="page-link btn-primary"
                @click="currentPage += 1"
                aria-label="Next"
              >
                <span aria-hidden="true">Next</span>
              </button>
            </li>
            <li
              class="page-item"
              :class="{ disabled: currentPage === pageCount }"
            >
              <button
                class="page-link btn-primary"
                @click="currentPage = pageCount"
                aria-label="Last page"
              >
                <span aria-hidden="true">Last</span>
              </button>
            </li>
          </ul>
        </div>
      </nav>
    </div>
  </div>
</template>

<script>
import xlsx from "json-as-xlsx";
import jsPDF from "jspdf";

export default {
  props: {
    uniqueID: {
      type: String,
      default: () => {
        const affix = "table";
        return `${affix}-${Math.random().toString(36).substring(7)}`;
      },
    },
    currentNoPage: {
      type: Number,
      default: 10,
    },
    mainHeaders: {
      type: Array,
      required: true,
    },
    mainItems: {
      type: Array,
      required: true,
    },
    subHeaders: {
      type: Array,
      required: true,
    },
    subHeaders2: {
      type: Array,
      required: true,
    },
    editable: {
      type: Boolean,
      required: true,
    },
    custombtn: {
      type: Boolean,
      required: true,
    },
    deletable: {
      type: Boolean,
      required: true,
    },
    toggleable: {
      type: Boolean,
      required: true,
    },
    slotsub: {
      type: Boolean,
      required: true,
    },
    selectable: {
      type: Boolean,
      required: true,
    },
    batchAction: {
      type: Boolean,
      required: false,
      default: false,
    },
    moreAction: {
      type: Boolean,
      required: false,
      default: false,
    },
    actionBtns: {
      type: Array,
      required: false,
    },
  },
  data() {
    return {
      isLoading: true,
      currentPage: 1,
      rowsPerPage: 10,
      showAll: false,
      showTable: {},
      searchText: "",
      sortColumn: null,
      sortDirection: 1,
      mainCheckbox: false,
      howmanyCheckbox: 0,
      getItemsfromCheckedBoxes: [],
    };
  },
  computed: {
    paginatedMainItems() {
      const startIndex = (this.currentPage - 1) * this.rowsPerPage;
      const endIndex = parseFloat(startIndex) + parseFloat(this.rowsPerPage);
      return this.filteredItems.slice(startIndex, endIndex);
    },
    filteredItems() {
      const sortedItems = [...this.mainItems];

      sortedItems.sort((a, b) => {
        const aValue = a[this.sortColumn];
        const bValue = b[this.sortColumn];
        let bool = this.sortDirection === 1 ? true : false;
        const aDate = Date.parse(aValue);
        const bDate = Date.parse(bValue);

        if (!isNaN(aDate) && !isNaN(bDate)) {
          // Sort dates
          return bool ? aDate - bDate : bDate - aDate;
        } else if (!isNaN(parseFloat(aValue)) && !isNaN(parseFloat(bValue))) {
          // Sort numbers numerically
          return bool
            ? parseFloat(aValue) - parseFloat(bValue)
            : parseFloat(bValue) - parseFloat(aValue);
        } else {
          // Sort strings alphabetically
          const aString = (aValue || "").toString().toLowerCase(); // Add check for undefined
          const bString = (bValue || "").toString().toLowerCase(); // Add check for undefined
          if (aString < bString) {
            return bool ? -1 : 1;
          } else if (aString > bString) {
            return bool ? 1 : -1;
          } else {
            return 0;
          }
        }
      });

      return sortedItems
        .map((o) => {
          if (o) {
            // Add check for undefined
            const searchCode =
              Object.keys(o)
                .map((key) => `${key}:${o[key]}`)
                .join("~") +
              (o.items
                ? o.items
                    .map((item) => Object.values(item).join(" "))
                    .join(", ")
                : []);
            return {
              ...o,
              searchCode,
            };
          }
        })
        .filter((item) =>
          item.searchCode
            .toString()
            .toLowerCase()
            .includes(this.searchText.toLowerCase())
        );
    },
    pageCount() {
      return Math.ceil(this.mainItems.length / this.rowsPerPage);
    },
    visiblePages() {
      let startPage = 1;
      let endPage = this.pageCount;
      if (this.pageCount > this.rowsPerPage) {
        const halfVisiblePages = Math.floor(this.rowsPerPage / 2);
        startPage = Math.max(this.currentPage - halfVisiblePages, 1);
        endPage = startPage + this.rowsPerPage - 1;
        if (endPage > this.pageCount) {
          endPage = this.pageCount;
          startPage = endPage - this.rowsPerPage + 1;
        } else if (startPage > 1) {
          startPage += 1;
        }
      }
      const pages = [];
      for (let i = startPage; i <= endPage; i++) {
        pages.push(i);
      }
      return pages;
    },
  },
  methods: {
    toggleCheckboxes() {
      this.mainCheckbox = !this.mainCheckbox;
      jQuery(".mtCheckbox").prop("checked", this.mainCheckbox);
      this.howmanyCheckbox = jQuery(".mtCheckbox").filter(":checked").length;
      let dataIds = [];
      this.getItemsfromCheckedBoxes = [];
      jQuery(".mtCheckbox")
        .filter(":checked")
        .each(function () {
          var dataId = jQuery(this).data("id");
          dataIds.push(dataId);
        });
      this.getItemsfromCheckedBoxes = dataIds;
    },
    toggleCheckbox() {
      this.howmanyCheckbox = jQuery(".mtCheckbox").filter(":checked").length;
      let dataIds = [];
      this.getItemsfromCheckedBoxes = [];
      jQuery(".mtCheckbox")
        .filter(":checked")
        .each(function () {
          var dataId = jQuery(this).data("id");
          dataIds.push(dataId);
        });
      this.getItemsfromCheckedBoxes = dataIds;
    },
    sort(field) {
      if (this.sortColumn === field) {
        this.sortDirection = -this.sortDirection;
      } else {
        this.sortColumn = field;
        this.sortDirection = 1;
      }
    },

    toggleAll() {
      const propKey = `showTable`;
      const toggleKey = `showAll`;
      this[toggleKey] = !this[toggleKey];
      this.filteredItems.forEach((item) => {
        this[propKey] = Object.assign({}, this[propKey], {
          [item.id]: this[toggleKey],
        });
      });
    },

    toggleTable(id) {
      this.showTable[id] = !this.showTable[id];
    },
    formatDate(date) {
      const options = {
        month: "2-digit",
        day: "2-digit",
        year: "numeric",
        hour: "numeric",
        minute: "numeric",
        second: "numeric",
      };
      return new Intl.DateTimeFormat("en-US", options).format(date);
    },

    sumColumn(col) {
      const total = this.paginatedMainItems.reduce(
        (accumulator, currentValue) =>
          accumulator + parseFloat(currentValue[col]),
        0
      );
      return total;
    },

    getObjectProperties(object) {
      return Object.keys(object).map((key) => {
        return {
          label: key,
          value: key,
        };
      });
    },

    transformData(jsonData) {
      const transformedData = [];

      jsonData.forEach((item) => {
        const mainRow = { ...item };

        // Remove items and items2 from the main row
        delete mainRow.items;
        delete mainRow.items2;

        // Add each item in 'items' as a new row under the main row
        item.items.forEach((itemRow) => {
          transformedData.push({ ...mainRow, ...itemRow });
        });

        // Add each item in 'items2' as a new row under the main row
        item.items2.forEach((itemRow) => {
          transformedData.push({ ...mainRow, ...itemRow });
        });
      });

      return transformedData;
    },

    exportXLSX() {
      let data = [
        {
          sheet: "data",
          columns: this.getObjectProperties(this.filteredItems[0]),
          content: this.filteredItems,
        },
      ];

      let settings = {
        fileName: "jsondata", // Name of the resulting spreadsheet
        extraLength: 3, // A bigger number means that columns will be wider
        writeMode: "writeFile", // The available parameters are 'WriteFile' and 'write'. This setting is optional. Useful in such cases https://docs.sheetjs.com/docs/solutions/output#example-remote-file
        writeOptions: {}, // Style options from https://docs.sheetjs.com/docs/api/write-options
        RTL: false, // Display the columns from right-to-left (the default value is false)
      };

      xlsx(data, settings); // Will download the excel file
    },

    saveAsPDF() {
      const doc = new jsPDF("l", "pt", [612, 936]);
      const content =
        "<div style='width:675pt'>" +
        document.getElementById(this.uniqueID).outerHTML +
        "</div>";
      doc.html(content, {
        callback: function (doc) {
          doc.save("download.pdf");
        },
      });
    },

    printSection() {
      // Add Bootstrap stylesheet to the head
      const bootstrapLink = document.createElement("link");
      bootstrapLink.rel = "stylesheet";
      bootstrapLink.href =
        "https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css";
      document.head.appendChild(bootstrapLink);

      // Create a progress bar element
      const progressBar = document.createElement("div");
      progressBar.className = "progress fixed-top";
      progressBar.innerHTML =
        '<div class="progress-bar progress-bar-striped progress-bar-animated" role="progressbar" style="width: 0%;" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100"></div>';

      // Add the progress bar to the body
      document.body.appendChild(progressBar);
      progressBar.style.zIndex = 1057;
      // Create the overlay element
      const overlay = document.createElement("div");
      overlay.style.position = "fixed";
      overlay.style.top = 0;
      overlay.style.left = 0;
      overlay.style.width = "100%";
      overlay.style.height = "100%";
      overlay.style.backgroundColor = "rgba(0, 0, 0, 0.5)";
      overlay.style.zIndex = 1056;
      overlay.classList.add("overlay");
      document.body.appendChild(overlay);

      // Track the loading progress of the stylesheet
      let progress = 0;
      const interval = setInterval(() => {
        progress += 10;
        if (progress >= 100) {
          clearInterval(interval);
          // Remove the progress bar
          document.body.removeChild(progressBar);
          // Get the dataTable section and create the print window
          const dataTable = document.getElementById(this.uniqueID);
          const printElement = document.createElement("div");
          printElement.appendChild(dataTable.cloneNode(true));

          // Open a new window and write the printElement to it
          const printWindow = window.open("", "Print Window");
          printWindow.document.write("<html><head>");
          printWindow.document.write(
            '<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">'
          );
          printWindow.document.write(
            "<style>html,body{display:none;}.no-print{display: none;} @media print{@page {size: legal landscape; margin:auto} html,body{display: block;} tr{page-break-inside: auto;} .no-print{display: none;}}</style>"
          );
          printWindow.document.write("</head><body>");
          printWindow.document.write(printElement.innerHTML);
          printWindow.document.write("</body></html>");
          printWindow.document.close();

          // Print the window and close it after printing
          printWindow.onload = function () {
            printWindow.focus();
            printWindow.print();
            printWindow.close();

            // Remove the Bootstrap stylesheet from the head
            document.head.removeChild(bootstrapLink);
            document.body.removeChild(overlay);
          };
        } else {
          // Update the progress bar
          const progressBarChild = progressBar.querySelector(".progress-bar");
          progressBarChild.style.width = `${progress}%`;
          progressBarChild.setAttribute("aria-valuenow", progress);
        }
      }, 200);
    },
  },
  mounted() {
    this.rowsPerPage = this.currentNoPage;
  },
};
</script>

<style scoped>
.badge-danger {
  background-color: #dc3545;
  color: #fff;
}
</style>
