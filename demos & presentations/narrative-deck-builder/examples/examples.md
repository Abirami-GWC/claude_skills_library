# Worked Examples

## Example 1: Retail, VPN instability (matches the ABC Retail use case)

**Input**
```
Customer Industry: Retail
Current Solution: Cisco ASA
Problems:
- VPN instability
- Compliance reporting
- Slow threat detection
Recommended Product: WatchGuard Firebox
```

**Processing notes**
- Story beat 1: open with retail-specific security stakes.
- Story beat 3: Cisco ASA gap framed relative to the three stated pains, not
  a generic "Cisco is bad" statement.
- Story beat 4: Firebox mapped to VPN instability, ThreatSync mapped to slow
  threat detection, compliance reporting mapped to Firebox's compliance
  reporting capability (all from knowledge.md).
- Story beat 6: "Retail Company" success story matched by industry.
- Story beat 7: Cisco ASA → Firebox migration, 2 weeks typical (knowledge.md).

**Output**
```
Presentation Outline

Slide 1
Modern Security Challenges in Retail

Slide 2
Challenges Faced by ABC Retail

Slide 3
Why Existing Infrastructure Falls Short

Slide 4
How WatchGuard Firebox Solves These Problems

Slide 5
Customer Success Story

Slide 6
Business Benefits

Slide 7
Migration Approach

Slide 8
Next Steps
```

## Example 2: Minimal input, single pain point

**Input**
```
Industry: Retail
Problem: VPN instability
Product: Firebox
```

**Output**
```
Slide 1
Retail Security Challenges

Slide 2
Current VPN Issues

Slide 3
Firebox Solution

Slide 4
Customer Success Story

Slide 5
Business Benefits

Slide 6
Next Steps
```
Note: fewer slides than Example 1 because there are fewer distinct pains and
no stated current-vendor migration context — no "Why Infrastructure Falls
Short" or "Migration Approach" slides were forced in.

## Example 3: No matching success story

**Input**
```
Industry: Logistics
Current Solution: SonicWall
Problems:
- Slow incident response
Recommended Product: ThreatSync
```

**Processing notes**
- No logistics-industry success story exists in knowledge.md.
- Rather than inventing one or reusing an unrelated industry's story as if it
  were a logistics story, the deck uses a placeholder and says so to the user.

**Output (Slide 5 only, shown for illustration)**
```
Slide 5
Customer Success Story
- [No logistics-specific success story on file yet — closest available match
  is the Retail Company story (45% fewer security incidents); recommend
  confirming with marketing before using it for a logistics customer]
```
