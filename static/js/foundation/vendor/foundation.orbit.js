$(document).foundation({
  orbit: {
    animation: 'slide',
    timer_speed: 100,
    pause_on_hover: true,
    animation_speed: 500,
    navigation_arrows: true,
    bullets: true
  }
});


$("#featured1").on("ready.fndtn.orbit", function(event) {
  console.info("ready");
});
$("#featured1").on("before-slide-change.fndtn.orbit", function(event) {
  console.info("before slide change");
});
$("#featured1").on("after-slide-change.fndtn.orbit", function(event, orbit) {
  console.info("after slide change");
  console.info("slide " + orbit.slide_number + " of " + orbit.total_slides);
});
$("#featured1").on("timer-started.fndtn.orbit", function(event, orbit) {
  console.info("timer started");
});
$("#featured1").on("timer-stopped.fndtn.orbit", function(event, orbit) {
  console.info("timer stopped");
});



.orbit-container {
  position: relative;
  height: 500px; }

.orbit-caption {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(10, 10, 10, 0.9); }

.orbit-caption p {
  position: relative;
  top: 50%;
  -webkit-transform: translateY(-50%);
  -ms-transform: translateY(-50%);
  transform: translateY(-50%);
  text-align: center;
  color: #fefefe;
  font-size: 48px;
  font-weight: 900; }

@media screen and (max-width: 39.9375em) {
  .orbit-caption p {
    font-size: 12px;
    font-weight: 400; } }
.orbit-bullets {
  display: none; }


$(document).foundation({
  orbit: {
      animation: 'slide', // Sets the type of animation used for transitioning between slides, can also be 'fade'
      timer_speed: 10000, // Sets the amount of time in milliseconds before transitioning a slide
      pause_on_hover: true, // Pauses on the current slide while hovering
      resume_on_mouseout: false, // If pause on hover is set to true, this setting resumes playback after mousing out of slide
      next_on_click: true, // Advance to next slide on click
      animation_speed: 500, // Sets the amount of time in milliseconds the transition between slides will last
      stack_on_small: false,
      navigation_arrows: true,
      slide_number: true,
      slide_number_text: 'of',
      container_class: 'orbit-container',
      stack_on_small_class: 'orbit-stack-on-small',
      next_class: 'orbit-next', // Class name given to the next button
      prev_class: 'orbit-prev', // Class name given to the previous button
      timer_container_class: 'orbit-timer', // Class name given to the timer
      timer_paused_class: 'paused', // Class name given to the paused button
      timer_progress_class: 'orbit-progress', // Class name given to the progress bar
      slides_container_class: 'orbit-slides-container', // Class name given to the slide container
      preloader_class: 'preloader', // Class given to the preloader
      slide_selector: 'li', // Default is '*' which selects all children under the container
      bullets_container_class: 'orbit-bullets',
      bullets_active_class: 'active', // Class name given to the active bullet
      slide_number_class: 'orbit-slide-number', // Class name given to the slide number
      caption_class: 'orbit-caption', // Class name given to the caption
      active_slide_class: 'active', // Class name given to the active slide
      orbit_transition_class: 'orbit-transitioning',
      bullets: true, // Does the slider have bullets visible?
      circular: true, // Does the slider should go to the first slide after showing the last?
      timer: true, // Does the slider have a timer active? Setting to false disables the timer.
      variable_height: false, // Does the slider have variable height content?
      swipe: true,
      before_slide_change: noop, // Execute a function before the slide changes
      after_slide_change: noop // Execute a function after the slide changes
  }
});

