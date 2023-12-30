<template>
  <div class="main-wrapper">
    <TopBar />

    <SideBar />

    <div class="page-wrapper">
      <div class="content container-fluid">
        <PageHeader />

        <router-view />
      </div>
      <FooterSection />
    </div>
  </div>
</template>
<script>
import TopBar from "../common/TopBar.vue";
import SideBar from "../common/SideBar.vue";
import PageHeader from "../common/PageHeader.vue";
import DashboardPage from "../main/DashboardPage.vue";
import FooterSection from "../common/FooterSection.vue";

import $ from "jquery";

export default {
  components: {
    TopBar,
    SideBar,
    PageHeader,
    DashboardPage,
    FooterSection,
  },
  mounted() {
    this.$router.push({ path: localStorage.getItem("savedPath") });
    ("use strict");
    $(document).ready(function () {
      if ($("#apexcharts-area").length > 0) {
        var options = {
          chart: { height: 350, type: "line", toolbar: { show: false } },
          dataLabels: { enabled: false },
          stroke: { curve: "smooth" },
          series: [
            {
              name: "Teachers",
              color: "#3D5EE1",
              data: [45, 60, 75, 51, 42, 42, 30],
            },
            {
              name: "Students",
              color: "#70C4CF",
              data: [24, 48, 56, 32, 34, 52, 25],
            },
          ],
          xaxis: {
            categories: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"],
          },
        };
        var chart = new ApexCharts(
          document.querySelector("#apexcharts-area"),
          options
        );
        chart.render();
      }
      if ($("#school-area").length > 0) {
        var options = {
          chart: { height: 350, type: "area", toolbar: { show: false } },
          dataLabels: { enabled: false },
          stroke: { curve: "straight" },
          series: [
            {
              name: "Teachers",
              color: "#3D5EE1",
              data: [45, 60, 75, 51, 42, 42, 30],
            },
            {
              name: "Students",
              color: "#70C4CF",
              data: [24, 48, 56, 32, 34, 52, 25],
            },
          ],
          xaxis: {
            categories: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"],
          },
        };
        var chart = new ApexCharts(
          document.querySelector("#school-area"),
          options
        );
        chart.render();
      }
      if ($("#bar").length > 0) {
        var optionsBar = {
          chart: {
            type: "bar",
            height: 350,
            width: "100%",
            stacked: false,
            toolbar: { show: false },
          },
          dataLabels: { enabled: false },
          plotOptions: { bar: { columnWidth: "55%", endingShape: "rounded" } },
          stroke: { show: true, width: 2, colors: ["transparent"] },
          series: [
            {
              name: "Boys",
              color: "#70C4CF",
              data: [
                420, 532, 516, 575, 519, 517, 454, 392, 262, 383, 446, 551,
              ],
            },
            {
              name: "Girls",
              color: "#3D5EE1",
              data: [
                336, 612, 344, 647, 345, 563, 256, 344, 323, 300, 455, 456,
              ],
            },
          ],
          labels: [
            2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019,
            2020,
          ],
          xaxis: {
            labels: { show: false },
            axisBorder: { show: false },
            axisTicks: { show: false },
          },
          yaxis: {
            axisBorder: { show: false },
            axisTicks: { show: false },
            labels: { style: { colors: "#777" } },
          },
          title: { text: "", align: "left", style: { fontSize: "18px" } },
        };
        var chartBar = new ApexCharts(
          document.querySelector("#bar"),
          optionsBar
        );
        chartBar.render();
      }
      if ($("#s-line").length > 0) {
        var sline = {
          chart: {
            height: 350,
            type: "line",
            zoom: { enabled: false },
            toolbar: { show: false },
          },
          dataLabels: { enabled: false },
          stroke: { curve: "straight" },
          series: [
            { name: "Desktops", data: [10, 41, 35, 51, 49, 62, 69, 91, 148] },
          ],
          title: { text: "Product Trends by Month", align: "left" },
          grid: { row: { colors: ["#f1f2f3", "transparent"], opacity: 0.5 } },
          xaxis: {
            categories: [
              "Jan",
              "Feb",
              "Mar",
              "Apr",
              "May",
              "Jun",
              "Jul",
              "Aug",
              "Sep",
            ],
          },
        };
        var chart = new ApexCharts(document.querySelector("#s-line"), sline);
        chart.render();
      }
    });
    if ($("#s-line-area").length > 0) {
      var sLineArea = {
        chart: { height: 350, type: "area", toolbar: { show: false } },
        dataLabels: { enabled: false },
        stroke: { curve: "smooth" },
        series: [
          { name: "series1", data: [31, 40, 28, 51, 42, 109, 100] },
          { name: "series2", data: [11, 32, 45, 32, 34, 52, 41] },
        ],
        xaxis: {
          type: "datetime",
          categories: [
            "2018-09-19T00:00:00",
            "2018-09-19T01:30:00",
            "2018-09-19T02:30:00",
            "2018-09-19T03:30:00",
            "2018-09-19T04:30:00",
            "2018-09-19T05:30:00",
            "2018-09-19T06:30:00",
          ],
        },
        tooltip: { x: { format: "dd/MM/yy HH:mm" } },
      };
      var chart = new ApexCharts(
        document.querySelector("#s-line-area"),
        sLineArea
      );
      chart.render();
    }
    if ($("#s-col").length > 0) {
      var sCol = {
        chart: { height: 350, type: "bar", toolbar: { show: false } },
        plotOptions: {
          bar: {
            horizontal: false,
            columnWidth: "55%",
            endingShape: "rounded",
          },
        },
        dataLabels: { enabled: false },
        stroke: { show: true, width: 2, colors: ["transparent"] },
        series: [
          { name: "Net Profit", data: [44, 55, 57, 56, 61, 58, 63, 60, 66] },
          { name: "Revenue", data: [76, 85, 101, 98, 87, 105, 91, 114, 94] },
        ],
        xaxis: {
          categories: [
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
          ],
        },
        yaxis: { title: { text: "$ (thousands)" } },
        fill: { opacity: 1 },
        tooltip: {
          y: {
            formatter: function (val) {
              return "$ " + val + " thousands";
            },
          },
        },
      };
      var chart = new ApexCharts(document.querySelector("#s-col"), sCol);
      chart.render();
    }
    if ($("#s-col-stacked").length > 0) {
      var sColStacked = {
        chart: {
          height: 350,
          type: "bar",
          stacked: true,
          toolbar: { show: false },
        },
        responsive: [
          {
            breakpoint: 480,
            options: {
              legend: { position: "bottom", offsetX: -10, offsetY: 0 },
            },
          },
        ],
        plotOptions: { bar: { horizontal: false } },
        series: [
          { name: "PRODUCT A", data: [44, 55, 41, 67, 22, 43] },
          { name: "PRODUCT B", data: [13, 23, 20, 8, 13, 27] },
          { name: "PRODUCT C", data: [11, 17, 15, 15, 21, 14] },
          { name: "PRODUCT D", data: [21, 7, 25, 13, 22, 8] },
        ],
        xaxis: {
          type: "datetime",
          categories: [
            "01/01/2011 GMT",
            "01/02/2011 GMT",
            "01/03/2011 GMT",
            "01/04/2011 GMT",
            "01/05/2011 GMT",
            "01/06/2011 GMT",
          ],
        },
        legend: { position: "right", offsetY: 40 },
        fill: { opacity: 1 },
      };
      var chart = new ApexCharts(
        document.querySelector("#s-col-stacked"),
        sColStacked
      );
      chart.render();
    }
    if ($("#s-bar").length > 0) {
      var sBar = {
        chart: { height: 350, type: "bar", toolbar: { show: false } },
        plotOptions: { bar: { horizontal: true } },
        dataLabels: { enabled: false },
        series: [
          { data: [400, 430, 448, 470, 540, 580, 690, 1100, 1200, 1380] },
        ],
        xaxis: {
          categories: [
            "South Korea",
            "Canada",
            "United Kingdom",
            "Netherlands",
            "Italy",
            "France",
            "Japan",
            "United States",
            "China",
            "Germany",
          ],
        },
      };
      var chart = new ApexCharts(document.querySelector("#s-bar"), sBar);
      chart.render();
    }
    if ($("#mixed-chart").length > 0) {
      var options = {
        chart: { height: 350, type: "line", toolbar: { show: false } },
        series: [
          {
            name: "Website Blog",
            type: "column",
            data: [440, 505, 414, 671, 227, 413, 201, 352, 752, 320, 257, 160],
          },
          {
            name: "Social Media",
            type: "line",
            data: [23, 42, 35, 27, 43, 22, 17, 31, 22, 22, 12, 16],
          },
        ],
        stroke: { width: [0, 4] },
        title: { text: "Traffic Sources" },
        labels: [
          "01 Jan 2001",
          "02 Jan 2001",
          "03 Jan 2001",
          "04 Jan 2001",
          "05 Jan 2001",
          "06 Jan 2001",
          "07 Jan 2001",
          "08 Jan 2001",
          "09 Jan 2001",
          "10 Jan 2001",
          "11 Jan 2001",
          "12 Jan 2001",
        ],
        xaxis: { type: "datetime" },
        yaxis: [
          { title: { text: "Website Blog" } },
          { opposite: true, title: { text: "Social Media" } },
        ],
      };
      var chart = new ApexCharts(
        document.querySelector("#mixed-chart"),
        options
      );
      chart.render();
    }
    if ($("#donut-chart").length > 0) {
      var donutChart = {
        chart: { height: 350, type: "donut", toolbar: { show: false } },
        series: [44, 55, 41, 17],
        responsive: [
          {
            breakpoint: 480,
            options: { chart: { width: 200 }, legend: { position: "bottom" } },
          },
        ],
      };
      var donut = new ApexCharts(
        document.querySelector("#donut-chart"),
        donutChart
      );
      donut.render();
    }
    if ($("#radial-chart").length > 0) {
      var radialChart = {
        chart: { height: 350, type: "radialBar", toolbar: { show: false } },
        plotOptions: {
          radialBar: {
            dataLabels: {
              name: { fontSize: "22px" },
              value: { fontSize: "16px" },
              total: {
                show: true,
                label: "Total",
                formatter: function (w) {
                  return 249;
                },
              },
            },
          },
        },
        series: [44, 55, 67, 83],
        labels: ["Apples", "Oranges", "Bananas", "Berries"],
      };
      var chart = new ApexCharts(
        document.querySelector("#radial-chart"),
        radialChart
      );
      chart.render();
    }
    (function ($) {
      "use strict";
      var $wrapper = $(".main-wrapper");
      var $pageWrapper = $(".page-wrapper");
      var $slimScrolls = $(".slimscroll");
      var Sidemenu = function () {
        this.$menuItem = $("#sidebar-menu a");
      };
      function init() {
        var $this = Sidemenu;
        $("#sidebar-menu a").on("click", function (e) {
          if ($(this).parent().hasClass("submenu")) {
            e.preventDefault();
          }
          if (!$(this).hasClass("subdrop")) {
            $("ul", $(this).parents("ul:first")).slideUp(350);
            $("a", $(this).parents("ul:first")).removeClass("subdrop");
            $(this).next("ul").slideDown(350);
            $(this).addClass("subdrop");
          } else if ($(this).hasClass("subdrop")) {
            $(this).removeClass("subdrop");
            $(this).next("ul").slideUp(350);
          }
        });
        $("#sidebar-menu ul li.submenu a.active")
          .parents("li:last")
          .children("a:first")
          .addClass("active")
          .trigger("click");
      }
      init();
      $("body").append('<div class="sidebar-overlay"></div>');
      $(document).on("click", "#mobile_btn", function () {
        $wrapper.toggleClass("slide-nav");
        $(".sidebar-overlay").toggleClass("opened");
        $("html").addClass("menu-opened");
        return false;
      });
      if ($(".toggle-password").length > 0) {
        $(document).on("click", ".toggle-password", function () {
          $(this).toggleClass("feather-eye feather-eye-off");
          var input = $(".pass-input");
          if (input.attr("type") == "password") {
            input.attr("type", "text");
          } else {
            input.attr("type", "password");
          }
        });
      }
      if ($(".reg-toggle-password").length > 0) {
        $(document).on("click", ".reg-toggle-password", function () {
          $(this).toggleClass("feather-eye feather-eye-off");
          var input = $(".pass-confirm");
          if (input.attr("type") == "password") {
            input.attr("type", "text");
          } else {
            input.attr("type", "password");
          }
        });
      }
      $(".sidebar-overlay").on("click", function () {
        $wrapper.removeClass("slide-nav");
        $(".sidebar-overlay").removeClass("opened");
        $("html").removeClass("menu-opened");
      });
      $(document).on("click", ".logo-hide-btn", function () {
        $(this).parent().hide();
      });
      if ($(".page-wrapper").length > 0) {
        var height = $(window).height();
        $(".page-wrapper").css("min-height", height);
      }
      $(window).resize(function () {
        if ($(".page-wrapper").length > 0) {
          var height = $(window).height();
          $(".page-wrapper").css("min-height", height);
        }
      });
      if ($(".select").length > 0) {
        $(".select").select2({ minimumResultsForSearch: -1, width: "100%" });
      }
      if ($("#editor").length > 0) {
        ClassicEditor.create(document.querySelector("#editor"), {
          toolbar: {
            items: [
              "heading",
              "|",
              "fontfamily",
              "fontsize",
              "|",
              "alignment",
              "|",
              "fontColor",
              "fontBackgroundColor",
              "|",
              "bold",
              "italic",
              "strikethrough",
              "underline",
              "subscript",
              "superscript",
              "|",
              "link",
              "|",
              "outdent",
              "indent",
              "|",
              "bulletedList",
              "numberedList",
              "todoList",
              "|",
              "code",
              "codeBlock",
              "|",
              "insertTable",
              "|",
              "uploadImage",
              "blockQuote",
              "|",
              "undo",
              "redo",
            ],
            shouldNotGroupWhenFull: true,
          },
        })
          .then((editor) => {
            window.editor = editor;
          })
          .catch((err) => {
            console.error(err.stack);
          });
      }
      $(".settings-form").on("click", ".trash", function () {
        $(this).closest(".links-cont").remove();
        return false;
      });
      $(document).on("click", ".add-links", function () {
        var experiencecontent =
          '<div class="row form-row links-cont">' +
          '<div class="form-group d-flex">' +
          '<button class="btn social-icon"><i class="feather-github"></i></button>' +
          '<input type="text" class="form-control" placeholder="Social Link">' +
          '<div><a href="#" class="btn trash"><i class="feather-trash-2"></i></a></div>' +
          "</div>" +
          "</div>";
        $(".settings-form").append(experiencecontent);
        return false;
      });
      if ($(".datetimepicker").length > 0) {
        $(".datetimepicker").datetimepicker({
          format: "DD-MM-YYYY",
          icons: {
            up: "fas fa-angle-up",
            down: "fas fa-angle-down",
            next: "fas fa-angle-right",
            previous: "fas fa-angle-left",
          },
        });
        $(".datetimepicker")
          .on("dp.show", function () {
            $(this)
              .closest(".table-responsive")
              .removeClass("table-responsive")
              .addClass("temp");
          })
          .on("dp.hide", function () {
            $(this)
              .closest(".temp")
              .addClass("table-responsive")
              .removeClass("temp");
          });
      }
      if ($('[data-toggle="tooltip"]').length > 0) {
        $('[data-toggle="tooltip"]').tooltip();
      }
      if ($(".datatable").length > 0) {
        $(".datatable").DataTable({ bFilter: false });
      }
      if ($(".datatables").length > 0) {
        $(".datatables").DataTable({ bFilter: true });
      }
      if ($(".zoom-screen .header-nav-list").length > 0) {
        $(".zoom-screen .header-nav-list").on("click", function (e) {
          if (!document.fullscreenElement) {
            document.documentElement.requestFullscreen();
          } else {
            if (document.exitFullscreen) {
              document.exitFullscreen();
            }
          }
        });
      }
      $(document).on("click", "#check_all", function () {
        $(".checkmail").click();
        return false;
      });
      if ($(".checkmail").length > 0) {
        $(".checkmail").each(function () {
          $(this).on("click", function () {
            if ($(this).closest("tr").hasClass("checked")) {
              $(this).closest("tr").removeClass("checked");
            } else {
              $(this).closest("tr").addClass("checked");
            }
          });
        });
      }
      $(document).on("click", ".mail-important", function () {
        $(this).find("i.fa").toggleClass("fa-star").toggleClass("fa-star-o");
      });
      if ($(".summernote").length > 0) {
        $(".summernote").summernote({
          height: 200,
          minHeight: null,
          maxHeight: null,
          focus: false,
        });
      }
      if ($slimScrolls.length > 0) {
        $slimScrolls.slimScroll({
          height: "auto",
          width: "100%",
          position: "right",
          size: "7px",
          color: "#ccc",
          allowPageScroll: false,
          wheelStep: 10,
          touchScrollStep: 100,
        });
        var wHeight = $(window).height() - 60;
        $slimScrolls.height(wHeight);
        $(".sidebar .slimScrollDiv").height(wHeight);
        $(window).resize(function () {
          var rHeight = $(window).height() - 60;
          $slimScrolls.height(rHeight);
          $(".sidebar .slimScrollDiv").height(rHeight);
        });
      }
      $(document).on("click", "#toggle_btn", function () {
        if ($("body").hasClass("mini-sidebar")) {
          $("body").removeClass("mini-sidebar");
          $(".subdrop + ul").slideDown();
        } else {
          $("body").addClass("mini-sidebar");
          $(".subdrop + ul").slideUp();
        }
        setTimeout(function () {}, 300);
        return false;
      });
      $(document).on("mouseover", function (e) {
        e.stopPropagation();
        if (
          $("body").hasClass("mini-sidebar") &&
          $("#toggle_btn").is(":visible")
        ) {
          var targ = $(e.target).closest(".sidebar").length;
          if (targ) {
            $("body").addClass("expand-menu");
            $(".subdrop + ul").slideDown();
          } else {
            $("body").removeClass("expand-menu");
            $(".subdrop + ul").slideUp();
          }
          return false;
        }
      });
      function animateElements() {
        $(".circle-bar1").each(function () {
          var elementPos = $(this).offset().top;
          var topOfWindow = $(window).scrollTop();
          var percent = $(this).find(".circle-graph1").attr("data-percent");
          var animate = $(this).data("animate");
          if (elementPos < topOfWindow + $(window).height() - 30 && !animate) {
            $(this).data("animate", true);
            $(this)
              .find(".circle-graph1")
              .circleProgress({
                value: percent / 100,
                size: 400,
                thickness: 30,
                fill: { color: "#6e6bfa" },
              });
          }
        });
        $(".circle-bar2").each(function () {
          var elementPos = $(this).offset().top;
          var topOfWindow = $(window).scrollTop();
          var percent = $(this).find(".circle-graph2").attr("data-percent");
          var animate = $(this).data("animate");
          if (elementPos < topOfWindow + $(window).height() - 30 && !animate) {
            $(this).data("animate", true);
            $(this)
              .find(".circle-graph2")
              .circleProgress({
                value: percent / 100,
                size: 400,
                thickness: 30,
                fill: { color: "#6e6bfa" },
              });
          }
        });
        $(".circle-bar3").each(function () {
          var elementPos = $(this).offset().top;
          var topOfWindow = $(window).scrollTop();
          var percent = $(this).find(".circle-graph3").attr("data-percent");
          var animate = $(this).data("animate");
          if (elementPos < topOfWindow + $(window).height() - 30 && !animate) {
            $(this).data("animate", true);
            $(this)
              .find(".circle-graph3")
              .circleProgress({
                value: percent / 100,
                size: 400,
                thickness: 30,
                fill: { color: "#6e6bfa" },
              });
          }
        });
      }
      if ($(".circle-bar").length > 0) {
        animateElements();
      }
      $(window).scroll(animateElements);
      $(window).on("load", function () {
        if ($("#loader").length > 0) {
          $("#loader").delay(350).fadeOut("slow");
          $("body").delay(350).css({ overflow: "visible" });
        }
      });
      $(".app-listing .selectBox").on("click", function () {
        $(this).parent().find("#checkBoxes").fadeToggle();
        $(this).parent().parent().siblings().find("#checkBoxes").fadeOut();
      });
      $(".invoices-main-form .selectBox").on("click", function () {
        $(this).parent().find("#checkBoxes-one").fadeToggle();
        $(this).parent().parent().siblings().find("#checkBoxes-one").fadeOut();
      });
      if ($(".SortBy").length > 0) {
        var show = true;
        var checkbox1 = document.getElementById("checkBox");
        $(".selectBoxes").on("click", function () {
          if (show) {
            checkbox1.style.display = "block";
            show = false;
          } else {
            checkbox1.style.display = "none";
            show = true;
          }
        });
      }
      $(function () {
        $("input[name='invoice']").click(function () {
          if ($("#chkYes").is(":checked")) {
            $("#show-invoices").show();
          } else {
            $("#show-invoices").hide();
          }
        });
      });
      $(".links-info-one").on("click", ".service-trash", function () {
        $(this).closest(".links-cont").remove();
        return false;
      });
      $(document).on("click", ".add-links", function () {
        var experiencecontent =
          '<div class="links-cont">' +
          '<div class="service-amount">' +
          '<a href="#" class="service-trash"><i class="fe fe-minus-circle me-1"></i>Service Charge</a> <span>$ 4</span' +
          "</div>" +
          "</div>";
        $(".links-info-one").append(experiencecontent);
        return false;
      });
      $(".links-info-discount").on("click", ".service-trash-one", function () {
        $(this).closest(".links-cont-discount").remove();
        return false;
      });
      $(document).on("click", ".add-links-one", function () {
        var experiencecontent =
          '<div class="links-cont-discount">' +
          '<div class="service-amount">' +
          '<a href="#" class="service-trash-one"><i class="fe fe-minus-circle me-1"></i>Offer new</a> <span>$ 4 %</span' +
          "</div>" +
          "</div>";
        $(".links-info-discount").append(experiencecontent);
        return false;
      });
      if ($("#summernote").length > 0) {
        $("#summernote").summernote({
          height: 300,
          minHeight: null,
          maxHeight: null,
          focus: true,
        });
      }
      if ($(".counter").length > 0) {
        $(".counter").counterUp({ delay: 20, time: 2000 });
      }
      if ($("#timer-countdown").length > 0) {
        $("#timer-countdown").countdown({
          from: 180,
          to: 0,
          movingUnit: 1000,
          timerEnd: undefined,
          outputPattern: "$day Day $hour : $minute : $second",
          autostart: true,
        });
      }
      if ($("#timer-countup").length > 0) {
        $("#timer-countup").countdown({ from: 0, to: 180 });
      }
      if ($("#timer-countinbetween").length > 0) {
        $("#timer-countinbetween").countdown({ from: 30, to: 20 });
      }
      if ($("#timer-countercallback").length > 0) {
        $("#timer-countercallback").countdown({
          from: 10,
          to: 0,
          timerEnd: function () {
            this.css({ "text-decoration": "line-through" }).animate(
              { opacity: 0.5 },
              500
            );
          },
        });
      }
      if ($("#timer-outputpattern").length > 0) {
        $("#timer-outputpattern").countdown({
          outputPattern: "$day Days $hour Hour $minute Min $second Sec..",
          from: 60 * 60 * 24 * 3,
        });
      }
      if ($('[data-bs-toggle="tooltip"]').length > 0) {
        var tooltipTriggerList = [].slice.call(
          document.querySelectorAll('[data-bs-toggle="tooltip"]')
        );
        var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
          return new bootstrap.Tooltip(tooltipTriggerEl);
        });
      }
      if ($(".popover-list").length > 0) {
        var popoverTriggerList = [].slice.call(
          document.querySelectorAll('[data-bs-toggle="popover"]')
        );
        var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
          return new bootstrap.Popover(popoverTriggerEl);
        });
      }
      if ($(".clipboard").length > 0) {
        var clipboard = new Clipboard(".btn");
      }
      $(".add-table-items").on("click", ".remove-btn", function () {
        $(this).closest(".add-row").remove();
        return false;
      });
      $(document).on("click", ".add-btn", function () {
        var experiencecontent =
          '<tr class="add-row">' +
          "<td>" +
          '<input type="text" class="form-control">' +
          "</td>" +
          "<td>" +
          '<input type="text" class="form-control">' +
          "</td>" +
          "<td>" +
          '<input type="text" class="form-control">' +
          "</td>" +
          "<td>" +
          '<input type="text" class="form-control">' +
          "</td>" +
          "<td>" +
          '<input type="text" class="form-control">' +
          "</td>" +
          "<td>" +
          '<input type="text" class="form-control">' +
          "</td>" +
          '<td class="add-remove text-end">' +
          '<a href="javascript:void(0);" class="add-btn me-2"><i class="fas fa-plus-circle"></i></a> ' +
          '<a href="#" class="copy-btn me-2"><i class="fe fe-copy"></i></a>' +
          '<a href="javascript:void(0);" class="remove-btn"><i class="fe fe-trash-2"></i></a>' +
          "</td>" +
          "</tr>";
        $(".add-table-items").append(experiencecontent);
        return false;
      });
      feather.replace();
    })(jQuery);
  },
};
</script>
