class DNAStrand:
    
    def __init__(self, dna:str):
        
        self.dna = dna
    
    def is_valid_dna(self)->bool:
        
        if not self.dna:
            return False
        
        valid_chars = ['A','C','T','G']
        
        for letter in set(self.dna):
            if letter not in valid_chars:
                return False
        
        return True

    def complement_WC(self)->str:
        
        if not self.is_valid_dna():
            return 'Invalid DNA'
        
        base_map = {
            'A' : 'T',
            'T' : 'A',
            'C' : 'G',
            'G' : 'C',
        }
        
        
        return ''.join([base_map[base] for base in self.dna])
    
    def palindrome_WC(self)->str:
        
        return self.complement_WC()[::-1]
    
    def contains_sequence(self, seq):
        
        return seq in self.dna
    
    def __str__(self):
        return self.dna
    
    @staticmethod
    def summarise(dna):
        
        print(f'Original DNA Sequence: {dna.dna}')
        
        if dna.is_valid_dna():
            print('Is valid')
            print('Complement: ', dna.complement_WC())
            print('WC Palindrome: ', dna.palindrome_WC())
        else:
            print('Not valid DNA')
    

dna_strand = DNAStrand('TTAACCGG')
DNAStrand.summarise(dna_strand)