# Worked Examples

## Example 1: Full notes (matches the ABC Manufacturing use case)

**Input**
```
Customer: ABC Manufacturing
Attendees: John Smith, Sarah Wilson
Topics Discussed:
- VPN Improvements
- Threat Detection
- Compliance Reporting
Questions:
- Pricing
- Migration Timeline
Requested Documents:
- Pricing Sheet
- Product Brochure
Next Meeting: Friday – 2:00 PM
```

**Output**
```
Subject: Thank You for Your Time Today

Hi John,

Thank you for taking the time to meet with us today.

During today's session we discussed:
- Improving VPN reliability
- Threat detection and response
- Compliance reporting capabilities

You also asked about pricing and migration timeline — we'll follow up with
details on both shortly.

As requested, we will share:
- Pricing Sheet
- Product Brochure

Our next meeting is scheduled for Friday at 2:00 PM.

Please let us know if you have any additional questions before then.

Looking forward to speaking with you again.

Best regards,
[Sales Representative Name]
WatchGuard Technologies
```

## Example 2: Minimal notes, no questions or documents

**Input**
```
Customer: ABC Manufacturing
Topics: VPN, Threat Detection
Next Meeting: Friday
```

**Output**
```
Subject: Thank You for Today's Meeting

Hi team,

Thank you for your time today.

Today's discussion included:
- VPN Improvements
- Threat Detection

Our next meeting is scheduled for Friday.

Looking forward to speaking with you again.

Best regards,
[Sales Representative Name]
WatchGuard Technologies
```
Note: no "Questions" or "Documents" section — the notes didn't include either,
so nothing was invented to fill those sections. Greeting defaults to "Hi team"
since no attendee name was given.

## Example 3: Missing next meeting date

**Input**
```
Customer: Northgate Logistics
Attendees: Maria Chen
Topics Discussed:
- Endpoint Security
Requested Documents:
- Technical Architecture Document
```

**Output**
```
Subject: Thank You for Your Time Today

Hi Maria,

Thank you for taking the time to meet with us today.

During today's session we discussed:
- Endpoint security capabilities

As requested, we will share:
- Technical Architecture Document

We'd love to find time to reconnect soon — let us know what works best on
your end.

Best regards,
[Sales Representative Name]
WatchGuard Technologies
```
Note: no specific next-meeting date/time was in the notes, so the email uses
a general reconnect line instead of inventing a date. Flag this gap to the
user: "No next meeting time was in your notes — you may want to confirm one
before sending."
