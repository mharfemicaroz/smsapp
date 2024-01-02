<template>
  <div class="row">
    <div class="col-sm-12">
      <div class="card">
        <div class="card-body">
          <form @submit.prevent="addProgram">
            <div class="row">
              <div class="col-12">
                <h5 class="form-title"><span>Program Info</span></h5>
              </div>
              <div class="col-12 col-sm-6">
                <div class="form-group">
                  <label
                    >Program Name <span class="login-danger">*</span></label
                  >
                  <input
                    type="text"
                    class="form-control"
                    placeholder="Program Name"
                    v-model="programInfo.name"
                    required
                  />
                </div>
              </div>
              <div class="col-12 col-sm-6">
                <div class="form-group">
                  <label>Major</label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="Major"
                    v-model="programInfo.major"
                  />
                </div>
              </div>
              <div class="col-12 col-sm-12">
                <div class="form-group">
                  <label>Description</label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="Description"
                    :value="computedDescription"
                    readonly
                  />
                </div>
              </div>
              <!-- Submit Button -->
              <div class="col-12">
                <div class="student-submit">
                  <button type="submit" class="btn btn-primary">Add</button>
                </div>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
  <div class="row">
    <div class="col-sm-12">
      <div class="card">
        <div class="card-body">
          <div class="table-responsive">
            <TableComponent
              :mainHeaders="headers"
              :mainItems="programs"
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
import ToasterComponent from "../common/ToasterComponent.vue";
import TableComponent from "../common/TableComponent.vue";
import { programApi } from "@/services/mainServices";
export default {
  components: {
    ToasterComponent,
    TableComponent,
  },
  data() {
    return {
      programInfo: {
        name: "",
        major: "",
      },
      headers: [
        {
          label: "ID",
          field: "id",
          sortable: true,
        },
        {
          label: "Name",
          field: "name",
          sortable: true,
        },
        {
          label: "Major",
          field: "major",
          sortable: true,
        },
        {
          label: "Description",
          field: "desc",
          sortable: true,
        },
        {
          label: "",
          field: "action",
          sortable: false,
        },
      ],
      programs: [],
    };
  },
  computed: {
    computedDescription() {
      if (this.programInfo.major) {
        return `${this.programInfo.name} major in ${this.programInfo.major}`;
      }
      return ""; // Clear the description if major is empty
    },
  },
  async created() {
    this.loadData();
  },
  methods: {
    async loadData() {
      this.programs = await programApi.fetchAll();
    },
    resetProgramInfo() {
      this.programInfo.name = "";
      this.programInfo.major = "";
    },
    async addProgram() {
      await programApi
        .filter({
          columnName: "desc",
          columnKey: this.programInfo.major
            ? `${this.programInfo.name} major in ${this.programInfo.major}`
            : this.programInfo.name,
        })
        .then(async (result) => {
          if (result.length > 0) {
            this.$refs.toast.showToast(
              "danger",
              "Program with this name and major already exists."
            );
          } else {
            try {
              const response = await programApi.add({
                name: this.programInfo.name,
                desc: this.programInfo.major
                  ? `${this.programInfo.name} major in ${this.programInfo.major}`
                  : this.programInfo.name,
                major: this.programInfo.major,
                // ... add other program fields if any ...
              });

              // Handle successful addition
              // For example, refresh the page or navigate to another view
              setTimeout(() => {
                this.$router.go(0);
              }, 1);
            } catch (error) {
              console.error(error);
              // Handle error
              // For example, show a toast notification
            }
          }
        });
    },
  },
};
</script>
