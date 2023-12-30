<template>
  <div class="row">
    <div class="col-sm-12">
      <div class="card">
        <div class="card-body">
          <form @submit.prevent="addStudent">
            <!-- Admission Info -->
            <div class="row">
              <div class="col-12">
                <h5 class="form-title"><span>Admission Info</span></h5>
              </div>
              <div class="col-12 col-sm-4">
                <div class="form-group">
                  <label>Student ID <span class="login-danger">*</span></label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="Student ID"
                    v-model="studentinfo.studentId"
                    required
                  />
                </div>
              </div>
              <div class="col-12 col-sm-4">
                <div class="form-group">
                  <label>Course <span class="login-danger">*</span></label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="Course"
                    v-model="studentinfo.course"
                    required
                  />
                </div>
              </div>
              <div class="col-12 col-sm-4">
                <div class="form-group">
                  <label>Major <span class="login-danger">*</span></label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="Major"
                    v-model="studentinfo.major"
                    required
                  />
                </div>
              </div>
            </div>

            <!-- Personal Info -->
            <div class="row">
              <div class="col-12">
                <h5 class="form-title"><span>Personal Info</span></h5>
              </div>
              <div class="col-12 col-sm-4">
                <div class="form-group">
                  <label>Last Name <span class="login-danger">*</span></label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="Last Name"
                    v-model="studentinfo.lastname"
                    required
                  />
                </div>
              </div>
              <div class="col-12 col-sm-4">
                <div class="form-group">
                  <label>First Name <span class="login-danger">*</span></label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="First Name"
                    v-model="studentinfo.firstname"
                    required
                  />
                </div>
              </div>
              <div class="col-12 col-sm-4">
                <div class="form-group">
                  <label>Middle Name</label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="Middle Name"
                    v-model="studentinfo.middlename"
                  />
                </div>
              </div>
              <div class="col-12 col-sm-4">
                <div class="form-group">
                  <label>Extension (e.g., Jr., Sr.)</label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="Extension"
                    v-model="studentinfo.extension"
                  />
                </div>
              </div>
              <div class="col-12 col-sm-4">
                <div class="form-group">
                  <label
                    >Date of Birth <span class="login-danger">*</span></label
                  >
                  <input
                    type="date"
                    class="form-control"
                    placeholder="DD-MM-YYYY"
                    v-model="studentinfo.birthdate"
                    required
                  />
                </div>
              </div>
              <div class="col-12 col-sm-4">
                <div class="form-group">
                  <label>Place of Birth</label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="Place of Birth"
                    v-model="studentinfo.birthplace"
                  />
                </div>
              </div>
              <div class="col-12 col-sm-4">
                <div class="form-group">
                  <label>Sex <span class="login-danger">*</span></label>
                  <select
                    class="form-control"
                    v-model="studentinfo.sex"
                    required
                  >
                    <option>Male</option>
                    <option>Female</option>
                    <option>Others</option>
                  </select>
                </div>
              </div>
              <div class="col-12 col-sm-4">
                <div class="form-group">
                  <label>Civil Status</label>
                  <select
                    class="form-control"
                    v-model="studentinfo.civilstatus"
                  >
                    <option>Single</option>
                    <option>Married</option>
                    <option>Widowed</option>
                    <option>Separated</option>
                    <option>Divorced</option>
                  </select>
                </div>
              </div>
              <div class="col-12 col-sm-4">
                <div class="form-group">
                  <label>Religion</label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="Religion"
                    v-model="studentinfo.religion"
                  />
                </div>
              </div>
              <div class="col-12 col-sm-4">
                <div class="form-group">
                  <label>Citizenship <span class="login-danger">*</span></label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="Citizenship"
                    v-model="studentinfo.citizenship"
                  />
                </div>
              </div>
              <div class="col-12 col-sm-4">
                <div class="form-group">
                  <label>Contact No. <span class="login-danger">*</span></label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="Contact No."
                    v-model="studentinfo.contactno"
                    required
                  />
                </div>
              </div>
              <div class="col-12 col-sm-4">
                <div class="form-group">
                  <label
                    >Email Address <span class="login-danger">*</span></label
                  >
                  <input
                    type="email"
                    class="form-control"
                    placeholder="Email Address"
                    v-model="studentinfo.email"
                    required
                  />
                </div>
              </div>
              <div class="col-12">
                <div class="form-group">
                  <label
                    >Permanent Address
                    <span class="login-danger">*</span></label
                  >
                  <input
                    type="text"
                    class="form-control"
                    placeholder="Permanent Address"
                    v-model="studentinfo.address"
                    required
                  />
                </div>
              </div>
              <div class="col-12 col-sm-4">
                <div class="form-group">
                  <label>Province</label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="Province"
                    v-model="studentinfo.province"
                  />
                </div>
              </div>
              <div class="col-12 col-sm-4">
                <div class="form-group">
                  <label>Municipality</label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="Municipality"
                    v-model="studentinfo.municipality"
                  />
                </div>
              </div>
              <div class="col-12 col-sm-4">
                <div class="form-group">
                  <label>Brgy</label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="Brgy"
                    v-model="studentinfo.brgy"
                  />
                </div>
              </div>
              <div class="col-12 col-sm-4">
                <div class="form-group">
                  <label>Postal Code</label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="Postal Code"
                    v-model="studentinfo.postal"
                  />
                </div>
              </div>
            </div>

            <!-- Family Background -->
            <div class="row">
              <div class="col-12">
                <h5 class="form-title"><span>Family Background</span></h5>
              </div>
              <!-- Father's Details -->
              <div class="col-12">
                <h6>Father's Details</h6>
              </div>
              <div class="col-12 col-sm-4">
                <div class="form-group">
                  <label>Name</label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="Father's Name"
                    v-model="studentinfo.fatherName"
                  />
                </div>
              </div>
              <div class="col-12 col-sm-4">
                <div class="form-group">
                  <label>Occupation</label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="Occupation"
                    v-model="studentinfo.fatherOccupation"
                  />
                </div>
              </div>
              <div class="col-12 col-sm-4">
                <div class="form-group">
                  <label>Contact No.</label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="Contact No."
                    v-model="studentinfo.fatherContactNo"
                  />
                </div>
              </div>

              <!-- Mother's Details -->
              <div class="col-12">
                <h6>Mother's Details</h6>
              </div>
              <div class="col-12 col-sm-4">
                <div class="form-group">
                  <label>Name</label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="Mother's Name"
                    v-model="studentinfo.motherName"
                  />
                </div>
              </div>
              <div class="col-12 col-sm-4">
                <div class="form-group">
                  <label>Occupation</label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="Occupation"
                    v-model="studentinfo.motherOccupation"
                  />
                </div>
              </div>
              <div class="col-12 col-sm-4">
                <div class="form-group">
                  <label>Contact No.</label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="Contact No."
                    v-model="studentinfo.motherContactNo"
                  />
                </div>
              </div>

              <!-- Guardian's Details (if applicable) -->
              <div class="col-12">
                <h6>Guardian's Details (if not living with parents)</h6>
              </div>
              <div class="col-12 col-sm-4">
                <div class="form-group">
                  <label>Name</label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="Guardian's Name"
                    v-model="studentinfo.guardianName"
                  />
                </div>
              </div>
              <div class="col-12 col-sm-4">
                <div class="form-group">
                  <label>Occupation</label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="Occupation"
                    v-model="studentinfo.guardianOccupation"
                  />
                </div>
              </div>
              <div class="col-12 col-sm-4">
                <div class="form-group">
                  <label>Contact No.</label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="Contact No."
                    v-model="studentinfo.guardianContactNo"
                  />
                </div>
              </div>

              <!-- In Case of Emergency -->
              <div class="col-12">
                <h6>In Case of Emergency</h6>
              </div>
              <div class="col-12 col-sm-4">
                <div class="form-group">
                  <label>Contact Person</label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="Contact Person's Name"
                    v-model="studentinfo.emergencyContactPerson"
                  />
                </div>
              </div>
              <div class="col-12 col-sm-4">
                <div class="form-group">
                  <label>Relationship</label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="Relationship"
                    v-model="studentinfo.emergencyRelationship"
                  />
                </div>
              </div>
              <div class="col-12 col-sm-4">
                <div class="form-group">
                  <label>Contact No.</label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="Contact No."
                    v-model="studentinfo.emergencyContactNo"
                  />
                </div>
              </div>
            </div>

            <!-- Educational Background -->
            <div class="row">
              <div class="col-12">
                <h5 class="form-title"><span>Educational Background</span></h5>
              </div>
              <!-- Junior High School -->
              <div class="col-12">
                <h6>Junior High School</h6>
              </div>
              <div class="col-12 col-sm-6">
                <div class="form-group">
                  <label>School Name</label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="School Name"
                    v-model="studentinfo.juniorHighSchoolName"
                  />
                </div>
              </div>
              <div class="col-12 col-sm-6">
                <div class="form-group">
                  <label>School Address</label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="School Address"
                    v-model="studentinfo.juniorHighSchoolAddress"
                  />
                </div>
              </div>
              <div class="col-12 col-sm-6">
                <div class="form-group">
                  <label>Inclusive Dates</label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="YYYY-YYYY"
                    v-model="studentinfo.juniorHighSchoolDates"
                  />
                </div>
              </div>

              <!-- Senior High School -->
              <div class="col-12">
                <h6>Senior High School</h6>
              </div>
              <div class="col-12 col-sm-6">
                <div class="form-group">
                  <label>School Name</label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="School Name"
                    v-model="studentinfo.seniorHighSchoolName"
                  />
                </div>
              </div>
              <div class="col-12 col-sm-6">
                <div class="form-group">
                  <label>School Address</label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="School Address"
                    v-model="studentinfo.seniorHighSchoolAddress"
                  />
                </div>
              </div>
              <div class="col-12 col-sm-6">
                <div class="form-group">
                  <label>Track</label>
                  <select
                    class="form-control"
                    v-model="studentinfo.seniorHighSchoolTrack"
                  >
                    <option value="academic">Academic</option>
                    <option value="techvoc">
                      Technical-Vocational-Livelihood
                    </option>
                    <option value="sportsarts">Sports and Arts</option>
                  </select>
                </div>
              </div>
              <div class="col-12 col-sm-6">
                <div class="form-group">
                  <label>Strand (if Academic Track)</label>
                  <select
                    class="form-control"
                    v-model="studentinfo.seniorHighSchoolStrand"
                  >
                    <option value="">Select Strand</option>
                    <option value="bam">
                      Business, Accountancy, Management (BAM)
                    </option>
                    <option value="hess">
                      Humanities, Education, Social Sciences (HESS)
                    </option>
                    <option value="stem">
                      Science, Technology, Engineering, Mathematics (STEM)
                    </option>
                  </select>
                </div>
              </div>
              <div class="col-12 col-sm-6">
                <div class="form-group">
                  <label>Inclusive Dates</label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="YYYY-YYYY"
                    v-model="studentinfo.seniorHighSchoolDates"
                  />
                </div>
              </div>

              <!-- Technical/Vocational Course (if applicable) -->
              <div class="col-12">
                <h6>Technical/Vocational Course (if applicable)</h6>
              </div>
              <div class="col-12 col-sm-6">
                <div class="form-group">
                  <label>Course Name</label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="Course Name"
                    v-model="studentinfo.vocationalCourseName"
                  />
                </div>
              </div>
              <div class="col-12 col-sm-6">
                <div class="form-group">
                  <label>School/Institution</label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="School/Institution"
                    v-model="studentinfo.vocationalSchoolName"
                  />
                </div>
              </div>
              <div class="col-12 col-sm-6">
                <div class="form-group">
                  <label>Inclusive Dates</label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="YYYY-YYYY"
                    v-model="studentinfo.vocationalCourseDates"
                  />
                </div>
              </div>

              <!-- College (if applicable) -->
              <div class="col-12">
                <h6>College (if applicable)</h6>
              </div>
              <div class="col-12 col-sm-6">
                <div class="form-group">
                  <label>College Name</label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="College Name"
                    v-model="studentinfo.collegeName"
                  />
                </div>
              </div>
              <div class="col-12 col-sm-6">
                <div class="form-group">
                  <label>College Address</label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="College Address"
                    v-model="studentinfo.collegeAddress"
                  />
                </div>
              </div>
              <div class="col-12 col-sm-6">
                <div class="form-group">
                  <label>Inclusive Dates</label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="YYYY-YYYY"
                    v-model="studentinfo.collegeDates"
                  />
                </div>
              </div>
            </div>

            <!-- Submit Button -->
            <div class="col-12">
              <div class="student-submit">
                <button type="submit" class="btn btn-primary">Submit</button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
  <ToasterComponent ref="toast" />
</template>
<script>
import ToasterComponent from "../common/ToasterComponent.vue";
import { studentApi } from "@/services/studentServices";
export default {
  components: {
    ToasterComponent,
  },
  data() {
    return {
      studentinfo: {
        studentId: "",
        course: "",
        major: "",
        lastname: "",
        firstname: "",
        middlename: "",
        extension: "",
        birthdate: "",
        birthplace: "",
        sex: "",
        civilstatus: "",
        religion: "",
        citizenship: "",
        contactno: "",
        email: "",
        address: "",
        province: "",
        municipality: "",
        brgy: "",
        postal: "",
        fatherName: "",
        fatherOccupation: "",
        fatherContactNo: "",
        motherName: "",
        motherOccupation: "",
        motherContactNo: "",
        guardianName: "",
        guardianOccupation: "",
        guardianContactNo: "",
        emergencyContactPerson: "",
        emergencyRelationship: "",
        emergencyContactNo: "",
        juniorHighSchoolName: "",
        juniorHighSchoolAddress: "",
        juniorHighSchoolDates: "",
        seniorHighSchoolName: "",
        seniorHighSchoolAddress: "",
        seniorHighSchoolTrack: "",
        seniorHighSchoolStrand: "",
        seniorHighSchoolDates: "",
        vocationalCourseName: "",
        vocationalSchoolName: "",
        vocationalCourseDates: "",
        collegeName: "",
        collegeAddress: "",
        collegeDates: "",
      },
    };
  },
  methods: {
    resetStudentInfo() {
      this.studentinfo.studentId = "";
      this.studentinfo.course = "";
      this.studentinfo.major = "";
      this.studentinfo.lastname = "";
      this.studentinfo.firstname = "";
      this.studentinfo.middlename = "";
      this.studentinfo.extension = "";
      this.studentinfo.birthdate = "";
      this.studentinfo.birthplace = "";
      this.studentinfo.sex = "";
      this.studentinfo.civilstatus = "";
      this.studentinfo.religion = "";
      this.studentinfo.citizenship = "";
      this.studentinfo.contactno = "";
      this.studentinfo.email = "";
      this.studentinfo.address = "";
      this.studentinfo.province = "";
      this.studentinfo.municipality = "";
      this.studentinfo.brgy = "";
      this.studentinfo.postal = "";
      this.studentinfo.fatherName = "";
      this.studentinfo.fatherOccupation = "";
      this.studentinfo.fatherContactNo = "";
      this.studentinfo.motherName = "";
      this.studentinfo.motherOccupation = "";
      this.studentinfo.motherContactNo = "";
      this.studentinfo.guardianName = "";
      this.studentinfo.guardianOccupation = "";
      this.studentinfo.guardianContactNo = "";
      this.studentinfo.emergencyContactPerson = "";
      this.studentinfo.emergencyRelationship = "";
      this.studentinfo.emergencyContactNo = "";
      this.studentinfo.juniorHighSchoolName = "";
      this.studentinfo.juniorHighSchoolAddress = "";
      this.studentinfo.juniorHighSchoolDates = "";
      this.studentinfo.seniorHighSchoolName = "";
      this.studentinfo.seniorHighSchoolAddress = "";
      this.studentinfo.seniorHighSchoolTrack = "";
      this.studentinfo.seniorHighSchoolStrand = "";
      this.studentinfo.seniorHighSchoolDates = "";
      this.studentinfo.vocationalCourseName = "";
      this.studentinfo.vocationalSchoolName = "";
      this.studentinfo.vocationalCourseDates = "";
      this.studentinfo.collegeName = "";
      this.studentinfo.collegeAddress = "";
      this.studentinfo.collegeDates = "";
    },
    async addStudent() {
      await studentApi
        .filter([
          {
            columnName: "firstname",
            columnKey: this.studentinfo.firstname,
          },
          {
            columnName: "lastname",
            columnKey: this.studentinfo.lastname,
          },
        ])
        .then(async (result) => {
          if (result.length > 0) {
            this.$refs.toast.showToast(
              "danger",
              "Student with this name already exists."
            );
            this.resetValues();
          } else {
            await studentApi
              .filter({
                columnName: "studentId",
                columnKey: this.studentinfo.studentId,
              })
              .then(async (result) => {
                if (result.length > 0) {
                  this.$refs.toast.showToast(
                    "danger",
                    "Student with this id code already exists."
                  );
                  this.resetValues();
                } else {
                  try {
                    const response = await studentApi.add({
                      studentId: this.studentinfo.studentId,
                      course: this.studentinfo.course,
                      major: this.studentinfo.major,
                      lastname: this.studentinfo.lastname,
                      firstname: this.studentinfo.firstname,
                      middlename: this.studentinfo.middlename,
                      extension: this.studentinfo.extension,
                      birthdate: this.studentinfo.birthdate,
                      birthplace: this.studentinfo.birthplace,
                      sex: this.studentinfo.sex,
                      civilstatus: this.studentinfo.civilstatus,
                      religion: this.studentinfo.religion,
                      citizenship: this.studentinfo.citizenship,
                      contactno: this.studentinfo.contactno,
                      email: this.studentinfo.email,
                      address: this.studentinfo.address,
                      province: this.studentinfo.province,
                      municipality: this.studentinfo.municipality,
                      brgy: this.studentinfo.brgy,
                      postal: this.studentinfo.postal,
                      fatherName: this.studentinfo.fatherName,
                      fatherOccupation: this.studentinfo.fatherOccupation,
                      fatherContactNo: this.studentinfo.fatherContactNo,
                      motherName: this.studentinfo.motherName,
                      motherOccupation: this.studentinfo.motherOccupation,
                      motherContactNo: this.studentinfo.motherContactNo,
                      guardianName: this.studentinfo.guardianName,
                      guardianOccupation: this.studentinfo.guardianOccupation,
                      guardianContactNo: this.studentinfo.guardianContactNo,
                      emergencyContactPerson:
                        this.studentinfo.emergencyContactPerson,
                      emergencyRelationship:
                        this.studentinfo.emergencyRelationship,
                      emergencyContactNo: this.studentinfo.emergencyContactNo,
                      juniorHighSchoolName:
                        this.studentinfo.juniorHighSchoolName,
                      juniorHighSchoolAddress:
                        this.studentinfo.juniorHighSchoolAddress,
                      juniorHighSchoolDates:
                        this.studentinfo.juniorHighSchoolDates,
                      seniorHighSchoolName:
                        this.studentinfo.seniorHighSchoolName,
                      seniorHighSchoolAddress:
                        this.studentinfo.seniorHighSchoolAddress,
                      seniorHighSchoolTrack:
                        this.studentinfo.seniorHighSchoolTrack,
                      seniorHighSchoolStrand:
                        this.studentinfo.seniorHighSchoolStrand,
                      seniorHighSchoolDates:
                        this.studentinfo.seniorHighSchoolDates,
                      vocationalCourseName:
                        this.studentinfo.vocationalCourseName,
                      vocationalSchoolName:
                        this.studentinfo.vocationalSchoolName,
                      vocationalCourseDates:
                        this.studentinfo.vocationalCourseDates,
                      collegeName: this.studentinfo.collegeName,
                      collegeAddress: this.studentinfo.collegeAddress,
                      collegeDates: this.studentinfo.collegeDates,
                    });

                    // localStorage.setItem("savedPath", "/index/customerlist/");
                    // this.$router.push(`/index/customerlist/`);
                    setTimeout(() => {
                      this.$router.go(0);
                    }, 1);
                  } catch (error) {
                    console.error(error);
                  }
                }
              });
          }
        });
    },
  },
};
</script>
