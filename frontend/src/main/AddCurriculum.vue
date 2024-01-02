<template>
  <div class="row">
    <div class="col-sm-12">
      <div class="card">
        <div class="card-body">
          <form @submit.prevent="addCurriculum">
            <div class="row">
              <div class="col-12">
                <h5 class="form-title"><span>Curriculum Info</span></h5>
              </div>
              <div class="col-12 col-sm-6">
                <div class="form-group">
                  <label>Name <span class="login-danger">*</span></label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="Name"
                    v-model="curriculum.name"
                    required
                  />
                </div>
              </div>
              <div class="col-12 col-sm-6">
                <div class="form-group">
                  <label>Description</label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="Description"
                    v-model="curriculum.description"
                  />
                </div>
              </div>
              <div class="col-12 col-sm-6">
                <div class="form-group">
                  <label>Program <span class="login-danger">*</span></label>
                  <select
                    class="form-control"
                    v-model="curriculum.program"
                    @change="changeProgram"
                  >
                    <option v-for="program in programs" :value="program.name">
                      {{ program.name }}
                    </option>
                  </select>
                </div>
              </div>
              <div class="col-12 col-sm-6">
                <div class="form-group">
                  <label
                    >Major
                    <span v-if="majors.length > 0" class="login-danger"
                      >*</span
                    ></label
                  >
                  <select
                    :disabled="majors.length === 0"
                    :required="majors.length > 0"
                    class="form-control"
                    v-model="curriculum.major"
                    @change="changeMajor"
                  >
                    <option v-for="major in majors" :value="major.id">
                      {{ major.major }}
                    </option>
                  </select>
                </div>
              </div>
              <!-- Submit Button -->
              <div class="col-12">
                <div class="student-submit">
                  <button type="submit" class="btn btn-primary">Submit</button>
                </div>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
  {{ currentCuriD }}
  <ToasterComponent ref="toast" />
</template>
<script>
import { programApi, curriculumApi } from "@/services/mainServices";
import ToasterComponent from "../common/ToasterComponent.vue";
export default {
  components: {
    ToasterComponent,
  },
  data() {
    return {
      currentCuriD: null,
      curriculum: {
        name: "",
        description: "",
        program: null,
        major: "",
      },
      programs: [],
      majors: [],
    };
  },
  async created() {
    this.loadData();
  },
  methods: {
    async loadData() {
      this.programs = await programApi.fetchAllDistinct("name");
    },
    async changeProgram() {
      this.majors = await programApi.filter({
        columnName: "name",
        columnKey: this.curriculum.program,
      });
      this.majors = this.majors.filter((item) => item.major !== "");
    },
    changeMajor() {
      this.currentCuriD = this.curriculum.major;
    },
    async addCurriculum() {
      await curriculumApi
        .filter({
          columnName: "name",
          columnKey: this.curriculum.name,
        })
        .then(async (result) => {
          if (result.length > 0) {
            this.$refs.toast.showToast(
              "danger",
              "Curriculum with this name already exists."
            );
            this.resetValues();
          } else {
            try {
              await curriculumApi.add({});
              setTimeout(() => {
                this.$router.go(0);
              }, 1);
            } catch (error) {
              console.error(error);
            }
          }
        });
    },
    resetValues() {
      this.curriculum = {
        name: "",
        description: "",
        program: null,
        major: "",
      };
    },
  },
};
</script>
