# Expose about page `academic_service` front matter as `site.data.academic_service`
# so the CV page can render the same content without duplicating YAML.
module AcademicServiceFromAbout
  class Generator < Jekyll::Generator
    safe true
    priority :lowest

    def generate(site)
      about = site.pages.find do |page|
        page.data['layout'] == 'about' && page.data['academic_service']
      end
      return unless about

      site.data['academic_service'] = about.data['academic_service']
    end
  end
end
