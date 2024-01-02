<template>
  <div class="row">
    <div class="col-sm-12">
      <div class="card">
        <div class="card-body">
          <form @submit.prevent="addSubject">
            <div class="row">
              <div class="col-12">
                <h5 class="form-title"><span>Subject Info</span></h5>
              </div>
              <div class="col-12 col-sm-4">
                <div class="form-group">
                  <label>Name <span class="login-danger">*</span></label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="Name"
                    v-model="subject.name"
                    required
                  />
                </div>
              </div>
              <div class="col-12 col-sm-8">
                <div class="form-group">
                  <label>Description <span class="login-danger">*</span></label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="Description"
                    v-model="subject.description"
                    required
                  />
                </div>
              </div>
              <div class="col-12 col-sm-4">
                <div class="form-group">
                  <label>Units <span class="login-danger">*</span></label>
                  <input
                    type="number"
                    class="form-control"
                    placeholder="Units"
                    v-model.number="subject.units"
                    required
                  />
                </div>
              </div>
              <div class="col-12 col-sm-4">
                <div class="form-group">
                  <label>Subtype <span class="login-danger">*</span></label>
                  <select class="form-control" v-model="subject.subtype">
                    <option value="Professional">Professional</option>
                    <option value="General">General</option>
                    <option value="Electives">General</option>
                    <option value="Specialization">Specialization</option>
                    <option value="Institutional Requirement">
                      Institutional Requirement
                    </option>
                  </select>
                </div>
              </div>
              <div class="col-12 col-sm-4">
                <div class="form-group">
                  <label>Prerequisites</label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="Prerequisites"
                    v-model="subject.prereq"
                  />
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
</template>
<script>
export default {
  data() {
    return {
      subject: {
        name: "",
        description: "",
        units: 0,
        subtype: "",
        prereq: "",
      },
    };
  },
  // Methods, computed properties, etc. can be added here as needed
};
</script>
