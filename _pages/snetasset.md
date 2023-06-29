---
layout: page-notitle
permalink: /snetasset/
title: snet-asset
pagination:
    enabled: true
    collection: "snet-asset"
    permalink: /page/:num/
    per_page: 15
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

<!-- Add a tag filter -->
<select id="tag-filter">
    <option value="all">All</option>
    {% for tag in site.data.tag %}
    <option value="{{ tag }}">{{ tag }}</option>
    {% endfor %}
</select>

<div class="infinite-scroll-gallery">
    <div class="image-gallery">
    <div class="sizer"></div>
    {% assign posts = paginator.posts | sort: 'tag' %}
    {% for video in posts %}
    <div class="image" data-tag="{{ video.tag }}">
        <video loop muted playsinline data-src="{{ video.src }}" type="video/mp4">
            Your browser does not support the video tag.
        </video>
        <div class="video-info">
            <p>Tag: {{ video.tag }}</p>
            <p>ID: {{ video.vid }}</p>
        </div>
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
  const POSTS_PER_PAGE = 15;
  var elem = document.querySelector('.image-gallery');
  console.log('Elem:', elem);
  
  var msnry = new Masonry( elem, {
    itemSelector: '.image', 
    columnWidth: '.sizer', 
    percentPosition: true
  });

  var infScroll = new InfiniteScroll( elem, {
    path: 'a.pagination__next',
    append: '.image',
    history: false,
    scrollThreshold: 0,
    status: '.page-load-status',
    debug: true,
    outlayer: msnry,
  });

  function updateVideos() {
    document.querySelectorAll('.image-gallery video[data-src]').forEach(function(video) {
      var rect = video.getBoundingClientRect();
      var isInViewport = rect.top <= window.innerHeight && rect.bottom >= 0;
      if (isInViewport) {
        video.src = video.getAttribute('data-src');
        video.removeAttribute('data-src');
        video.load();
      }
    });
  }

  function initializeVideo(video) {
    video.onloadeddata = function() {
      console.log('Video data loaded.');
      msnry.layout();
      video.play().catch(function(error) {
        console.error('Error attempting to play:', error);
      });
    };

    video.onerror = function() {
      console.error('Error loading video:', video.src);
      video.parentElement.style.display = 'none';
    };
    
    updateVideos();
  }

  document.querySelectorAll('.image-gallery video').forEach(initializeVideo);

  infScroll.on('append', function(response, path, items) {
    console.log('InfScroll append event triggered.');
    items.forEach(function(item) {
      var video = item.querySelector('video');
      if (video) {
        initializeVideo(video);
      }
    });
    filterVideos(tagFilter.value);
    checkVisibleImages();
    msnry.layout();
  });
  
  window.addEventListener('scroll', updateVideos);
  window.addEventListener('resize', updateVideos);
  window.addEventListener('resize', function() {
    msnry.layout();
  });
  
  var tagFilter = document.getElementById('tag-filter');
  
  function filterVideos(tag) {
    console.log('Filtering videos for tag:', tag);
    var images = document.querySelectorAll('.image');
    images.forEach(function(image) {
      if (tag === 'all' || image.getAttribute('data-tag') === tag) {
        image.style.display = '';
      } else {
        image.style.display = 'none';
      }
    });

    msnry.layout();
  }

  tagFilter.addEventListener('change', function(event) {
    console.log('Tag filter changed:', event.target.value);
    filterVideos(event.target.value);
    infScroll.loadNextPage();
    msnry.layout();
  });
  
  function checkVisibleImages() {
    var images = document.querySelectorAll('.image:not([style*="display: none"])');
    if (images.length < POSTS_PER_PAGE) {
      infScroll.loadNextPage();
      msnry.layout();
    }
  }
});
</script>


