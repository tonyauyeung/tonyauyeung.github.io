---
title: 'Blogs'
date: 2024-09-23
type: landing

design:
  # Section spacing
  spacing: '5rem'

# Page sections
sections:
  # - block: collection
  #   content:
  #     title: Selected Blogs
  #     text: I enjoy making things. Here are a selection of projects that I have worked on over the years.
  #     filters:
  #       folders:
  #         - blog
  #   # design:
  #   #   view: article-grid
  #   #   fill_image: false
  #   #   columns: 1
  - block: collection
    content:
      title: Blogs
      subtitle: ''
      text: 'I enjoy making things. Here are a selection of projects that I have worked on over the years.'
      # Page type to display. E.g. post, talk, publication...
      page_type: post
      # Choose how many pages you would like to display (0 = all pages)
      count: 5
      # Filter on criteria
      filters:
        author: admin
        category: ""
        tag: ""
        exclude_featured: false
        exclude_future: false
        exclude_past: false
        publication_type: ""
      # Choose how many pages you would like to offset by
      offset: 0
      # Page order: descending (desc) or ascending (asc) date.
      order: desc
    design:
      # Choose a layout view
      view: date-title-summary
      # Reduce spacing
      spacing:
        padding: [0, 0, 0, 0]
---