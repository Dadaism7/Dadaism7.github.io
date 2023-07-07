---
layout: page-notitle
permalink: /snetasset/
title: snet-asset
pagination:
    enabled: true
    collection: "snet-asset"
    permalink: /page/:num/
    per_page: 15
    sort_field: 'order'
    sort_reverse: false
    trail:
    before: 1 # The number of links before the current page
    after: 3  # The number of links after the current page
    indexpage: 'snet-asset'
---
<header class="post-header center-text">
    <h1 class="post-title">ScenarioNet Demo</h1>
</header>
<div style="text-align: center;">
  <p>For faster loading times, we have compressed our videos.</p>
  <p>For optimal viewing experience, we recommend accessing this website on a computer.</p>
</div>
<div id="tag-filter">
    <button class="filter-button" data-tag="all">All</button>
    {% for tag in site.data.tag %}
    <button class="filter-button" data-tag="{{ tag }}">{{ tag }}</button>
    {% endfor %}
</div>

<div class="infinite-scroll-gallery">
    <div class="image-gallery">
    <div class="sizer"></div>
    {% assign posts = paginator.posts | sort: 'order' %}
    {% for video in posts %}
    <div class="image" data-tag="{{ video.tag }}">
        <video loop muted playsinline>
            <source src="{{ video.src }}" type="video/mp4">
            <source src="{{ video.src }}" type="video/webm">
            Your browser does not support the video tag.
        </video>
        <div class="video-info" style="display: flex; justify-content: center; align-items: center; flex-direction: row; gap: 10px;">
            <div class="badge badge-tag">{{ video.tag }}</div>
            <div class="badge badge-id">{{ video.vid }}</div>
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
function shuffleArray(array) {
  for (let i = array.length - 1; i > 0; i--) {
    let j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
  return array;
}
document.addEventListener('DOMContentLoaded', function() {
  const POSTS_PER_PAGE = 15;
  var elem = document.querySelector('.image-gallery');
  
  var msnry = new Masonry( elem, {
    itemSelector: '.image', 
    columnWidth: '.sizer', 
    percentPosition: true
  });

  var imageElements = Array.from(document.querySelectorAll('.image'));
  shuffleArray(imageElements);
  imageElements.forEach(function(imageElement) {
    elem.appendChild(imageElement);
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
    document.querySelectorAll('.image-gallery video[src]').forEach(function(video) {
      var rect = video.getBoundingClientRect();
      var isInViewport = rect.top <= window.innerHeight && rect.bottom >= 0;
      if (isInViewport) {
        video.src = video.getAttribute('src');
        video.removeAttribute('src');
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
    shuffleArray(Array.from(items));
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
  
    var filterButtons = document.querySelectorAll('.filter-button');

  
    function filterVideos(tag) {
      console.log('Filtering videos for tag:', tag);
      var images = document.querySelectorAll('.image');
      images.forEach(function(image) {
        var video = image.querySelector('video');
        if (tag === 'all' || image.getAttribute('data-tag') === tag) {
          image.style.display = '';
          // If the video has not been loaded yet, load it now
          if (video.getAttribute('src')) {
            video.src = video.getAttribute('src');
            video.removeAttribute('src');
            video.load();
          }
        } else {
          image.style.display = 'none';
          // If the video has been loaded, unload it
          if (!video.getAttribute('src')) {
            video.setAttribute('src', video.src);
            video.src = '';
          }
        }
      });
    
      msnry.layout();
    }


filterButtons.forEach(function(button) {
    button.addEventListener('click', function(event) {
        console.log('Tag filter changed:', event.target.dataset.tag);
        filterVideos(event.target.dataset.tag);
        infScroll.loadNextPage();
        msnry.layout();

        // Remove the 'active' class from all buttons
        filterButtons.forEach(function(btn) {
            btn.classList.remove('active');
        });

        // Add the 'active' class to the clicked button
        event.target.classList.add('active');
    });
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


