RSpec.describe BackupPostCrawler, type: :apis do
  describe 'backup_post_crawler' do
    let(:request) do
      stub_request(:post, "https://sandbox.f1sales.org/public/integrations/crawlers/#{crawler.id}/leads")
        .with(body_request)
    end
    let(:body_request) do
      {
        "lead": {
          "customer": {
            "name": 'customer_name',
            "phone": 'customer_phone',
            "email": 'customer_email'
          },
          "product": {
            "name": 'product_name' 
          },
          "dealership": {
            "id": "",
            "account": "" 
          },
          "origin_url": 'url_lead'
        },
        "crawler_id": "64077272771cf900d926aa45"
      }
    end
  end
end
