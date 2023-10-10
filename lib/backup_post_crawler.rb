require 'json'
require 'http'

file = File.open 'leads_payload.json'
json_file = JSON.load file

leads = json_file['leads']

leads.each do |lead|
  HTTP.post('https://sandbox.f1sales.org/public/integrations/crawlers/65254f5394371400013cff72/leads', json: lead)
end
