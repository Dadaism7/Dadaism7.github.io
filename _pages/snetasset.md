---
layout: page-notitle
permalink: /snetasset/
title: snet-asset
pagination:
    enabled: true
    collection: "snet-asset"
    permalink: /page/:num/
    per_page: 12
    sort_field: date
    sort_reverse: true
    trail:
    before: 1 # The number of links before the current page
    after: 3  # The number of links after the current page
    indexpage: 'snet-asset'
---
<header class="post-header center-text">
    <h1 class="post-title">ScenarioNet Demo</h1>
</header>
<div class="infinite-scroll-gallery">
    <div class="image-gallery">
    {% for video in paginator.posts %}
    <div class="image">
        <video loop muted playsinline data-src="{{ video.src }}" type="video/mp4">
            Your browser does not support the video tag.
        </video>
    </div>
    {% endfor %}
    </div>
    {% if paginator.next_page %}
    <div class="pagination">
        <a href="{{ paginator.next_page_path }}" class="pagination__next">Next</a>
    </div>
    {% endif %}
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  var elem = document.querySelector('.image-gallery');
  var msnry = new Masonry( elem, {
    itemSelector: '.image', 
    columnWidth: '.image', 
    percentPosition: true
  });

  function updateColumnWidth() {
    var aspectRatio = window.innerWidth / window.innerHeight;
    if (aspectRatio < 1) {
      // If it's portrait
      msnry.options.columnWidth = elem.offsetWidth;
    } else {
      // If it's landscape
      msnry.options.columnWidth = '.image';
    }
    msnry.layout();
  }
  
  updateColumnWidth();
  window.addEventListener('resize', updateColumnWidth);

  var infScroll = new InfiniteScroll( elem, {
    path: 'a.pagination__next',
    append: '.image',
    history: false,
    scrollThreshold: 0,
    status: '.page-load-status',
    debug: true,
    outlayer: msnry,  // use Masonry as the layout view
  });

  var observer = new IntersectionObserver(function(entries) {
    entries.forEach(function(entry) {
      if (entry.isIntersecting) {
        var video = entry.target;
        if (video) {
          video.src = video.getAttribute('data-src');
          video.load();
        }
      }
    });
  }, {
    rootMargin: '100px' // load when the video is within 100px from the viewport
  });

  function initializeVideo(video) {
    video.onloadeddata = function() {
      msnry.layout();
      video.play().catch(function(error) {
        console.log('Error attempting to play:', error);
      });
    };

    video.onerror = function() {
      console.log('Error loading video:', video.src);
      video.parentElement.style.display = 'none'; // Hide the video
    };

    observer.observe(video);
  }

  document.querySelectorAll('.image-gallery video').forEach(initializeVideo);

  infScroll.on('append', function(response, path, items) {
    items.forEach(function(item) {
      var video = item.querySelector('video');
      if (video) {
        initializeVideo(video);
      }
    });
  });
  window.addEventListener('resize', function() {
    msnry.layout();
  });
});
</script>






