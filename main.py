import decoder
import kofig

if __name__ == '__main__':
    decoder.decodeABI(
        rpc=kofig.rpc, 
        address=kofig.address,
    )
