import random as rd

# dicionario com todos os aeroportos do Brasil por estados e cidades
aeroportos = {
    'AC': {
        'RBR': 'Aeroporto Internacional de Rio Branco/Placido de Castro', 
        'CZS': 'Aeroporto Internacional de Cruzeiro do Sul'
        },
    'AM': {
        'MAO': 'Aeroporto Internacional de Manaus/Eduardo Gomes'
        }, 
    'RO': {
        'PVH': 'Aeroporto Internacional de Porto Velho/Governador Jorge Teixeira de Oliveira'
        }, 
    'RR': {
        'BVB': 'Aeroporto Internacional de Boa Vista/Atlas Brasil Cantanhede'
        }, 
    'AP': {
        'MCP': 'Aeroporto Internacional de Macapa'
        }, 
    'PA': {
        'BEL': 'Aeroporto Internacional de Belem/Val de Cans', 
        'STM': 'Aeroporto de Santarem/Maestro Wilson Fonseca', 
        'MAB': 'Aeroporto de Marabá'
        }, 
    'TO': {
        'PMW': 'Aeroporto de Palmas/Brigadeiro Lysias Rodrigues'
        }, 
    'AL': {
        'MCZ': 'Aeroporto de Maceio/Zumbi dos Palmares'
        }, 
    'BA': {
        'SSA': 'Aeroporto Internacional de Salvador/Deputado Luis Eduardo Magalhães',
        'BPS': 'Aeroporto Internacional de Porto Seguro',
        'IOS': 'Aeroporto de Ilheus/Bahia-Jorge Amado'
        }, 
    'CE': {
        'FOR': 'Aeroporto Internacional de Fortaleza/Pinto Martins',
        'JDO': 'Aeroporto de Juazeiro do Norte–Orlando Bezerra',
        }, 
    'MA': {
        'SLZ': 'Aeroporto Internacional de São Luis/Marechal Cunha Machado',
        'IMP': 'Aeroporto de Imperatriz–Prefeito Renato Moreira',
        }, 
    'PB': {
        'JPA': 'Aeroporto Internacional de Joao Pessoa/Presidente Castro Pinto',
        'CPV': 'Aeroporto de Campina Grande/Presidente Joao Suassuna',
        }, 
    'PI': {
        'THE': 'Aeroporto de Teresina–Senador Petronio Portella',
        }, 
    'PE': {
        'REC': 'Aeroporto Internacional do Recife/Guararapes–Gilberto Freyre',
        'PNZ': 'Aeroporto de Petrolina/Senador Nilo Coelho',
        'FER': 'Aeroporto de Fernando de Noronha'
        }, 
    'RN': {
        'NAT': 'Aeroporto Internacional de Natal/Augusto Severo',
        }, 
    'SE': {
        'AJU': 'Aeroporto Internacional de Aracaju/Santa Maria',
        }, 
    'GO': {
        'GYN': 'Aeroporto de Goiania/Santa Genoveva',
        }, 
    'MT': {
        'CGB': 'Aeroporto Internacional de Cuiaba/Marechal Rondon',
        }, 
    'MS': {
        'CGR': 'Aeroporto Internacional de Campo Grande',
        }, 
    'DF': {
        'BSB': 'Aeroporto Internacional de Brasilia/Presidente Jucelino Kubitschek',
        }, 
    'SP': {
        'CGH': 'Aeroporto Internacional de Sao Paulo/Congonhas',
        'VCP': 'Aeroporto Internacional de Viracopos/Campinas',
        'GRU': 'Aeroporto Internacional de Sao Paulo/Guarulhos-Governador Andre Franco Motoro',
        'PPB': 'Aeroporto Estadual de Presidente Prudente',
        'JTC': 'Aeroporto Estadual de Bauru/Arealva'
        }, 
    'RJ': {
        'GIG': 'Aeroporto Internacional do Rio de Janeiro/Galeao-Antonio Carlos Jobim',
        'SDU': 'Aeroporto Santos Dumont',
        'CFB': 'Aeroporto Internacional de Cabo Frio'
        }, 
    'ES': {
        'VIX': 'Aeroporto de Vitoria–Eurico de Aguiar Salles'
        }, 
    'MG': {
        'UDI': 'Aeroporto de Uberlandia/Ten. Cel. Av. Cesar Bombonato',
        'CNF': 'Aeroporto Internacional de Minas Gerais/Confins–Tancredo Neves',
        'MOC': 'Aeroporto de Montes Claros/Mario Ribeiro'
        }, 
    'SC': {
        'FLN': 'Aeroporto Internacional de Florianopolis/Hercilio Luz',
        'NVT': 'Aeroporto Internacional de Navegantes/Ministro Victor Konder',
        'JOI': 'Aeroporto de Joinville/Lauro Carneiro de Loyola',
        'XAP': 'Aeroporto de Chapeco–Serafin Enoss Bertaso'
        }, 
    'RS': {
        'POA': 'Aeroporto Internacional de Porto Alegre/Salgado Filho',
        'CXJ': 'Aeroporto Regional de Caxias do Sul/Hugo Cantergiani'
        }, 
    'PR': {
        'CWB': 'Aeroporto Internacional de Curitiba/Afonso Pena',
        'MGF': 'Aeroporto Regional de Maringá/Silvio Name Junior',
        'LDB': 'Aeroporto de Londrina/Governador Jose Richa',
        'IGU': 'Aeroporto Internacional de Foz do Iguacu'
        }
    }

estados = []
for i in aeroportos.keys():
    estados.append(i)

def gera_aeroporto():
    estado_escolhido = estados[rd.randrange(0, len(estados))]
    aeroporto_escolhido = aeroportos[estado_escolhido]
    cidades_possiveis = list(aeroporto_escolhido.keys())
    cidade_escolhida = cidades_possiveis[rd.randrange(0, len(cidades_possiveis))]

    aeroporto = (aeroporto_escolhido[cidade_escolhida], 'BR', estado_escolhido, cidade_escolhida)
    
    return aeroporto