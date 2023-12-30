<template>
  <div class="student-group-form">
    <div class="row">
      <div class="col-lg-3 col-md-6">
        <div class="form-group">
          <input
            type="text"
            class="form-control"
            placeholder="Search by ID ..."
          />
        </div>
      </div>
      <div class="col-lg-3 col-md-6">
        <div class="form-group">
          <input
            type="text"
            class="form-control"
            placeholder="Search by Name ..."
          />
        </div>
      </div>
      <div class="col-lg-4 col-md-6">
        <div class="form-group">
          <input
            type="text"
            class="form-control"
            placeholder="Search by Phone ..."
          />
        </div>
      </div>
      <div class="col-lg-2">
        <div class="search-student-btn">
          <button type="btn" class="btn btn-primary">Search</button>
        </div>
      </div>
    </div>
  </div>
  <div class="row">
    <div class="col-sm-12">
      <div class="card card-table comman-shadow">
        <div class="card-body">
          <div class="page-header">
            <div class="row align-items-center">
              <div class="col">
                <h3 class="page-title">Students</h3>
              </div>
              <div class="col-auto text-end float-end ms-auto download-grp">
                <a href="students.html" class="btn btn-outline-gray me-2 active"
                  ><i class="feather-list"></i
                ></a>
                <a href="students-grid.html" class="btn btn-outline-gray me-2"
                  ><i class="feather-grid"></i
                ></a>
                <a href="#" class="btn btn-outline-primary me-2"
                  ><i class="fas fa-download"></i> Download</a
                >
                <a href="add-student.html" class="btn btn-primary"
                  ><i class="fas fa-plus"></i
                ></a>
              </div>
            </div>
          </div>

          <div class="table-responsive">
            <TableComponent
              :mainHeaders="headers"
              :mainItems="filteredStudents"
              :editable="true"
              @edit-action="editAction"
            />
          </div>
        </div>
      </div>
    </div>
  </div>
  <ToasterComponent ref="toast" />
</template>
<script>
import TableComponent from "../common/TableComponent.vue";
import ToasterComponent from "../common/ToasterComponent.vue";
import { studentApi } from "@/services/studentServices";
export default {
  components: {
    TableComponent,
    ToasterComponent,
  },
  data() {
    return {
      headers: [
        {
          label: "ID",
          field: "studentId",
        },
        {
          label: "Full Name",
          field: "fullname",
        },
        {
          label: "Course",
          field: "course",
        },
        {
          label: "Major",
          field: "major",
        },
        {
          label: "Sex",
          field: "sex",
        },
        {
          label: "Birth Date",
          field: "birth",
        },
        {
          label: "Address",
          field: "address",
        },
        {
          label: "Contact No.",
          field: "contactno",
        },
        {
          label: "Email",
          field: "email",
        },
        {
          label: "",
          field: "action",
          sortable: false,
        },
      ],
      students: [],
    };
  },
  computed: {
    filteredStudents() {
      return this.students.map((o) => {
        const fullname =
          o.lastname +
          ", " +
          o.firstname +
          (o.middlename === "" ? "" : " " + o.middlename);
        const birthdate = new Date(o.birthdate).toLocaleDateString("en-US");
        return {
          ...o,
          fullname: fullname,
          birth: birthdate,
        };
      });
    },
  },
  async created() {
    this.loadData();
  },
  methods: {
    async loadData() {
      this.students = await studentApi.fetchAll();
    },
  },
};
</script>
