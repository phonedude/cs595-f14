#!/usr/bin/perl 

$webpage = $ARGV[0]; 


use WWW::Google::PageRank; 
my $pagerank = WWW::Google::PageRank->new; 
my $score = $pagerank->get($webpage);
if($score == "")
{
		$score = 0;
}

print scalar($score), "\n"; 
